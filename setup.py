from setuptools import find_packages, setup

def parse_requirements(fname='requirements.txt', with_version=True): # 解析requirements.txt文件
    """Parse the package dependencies listed in a requirements file but strips
    specific versioning information.

    Args:
        fname (str): path to requirements file
        with_version (bool, default=False): if True include version specs

    Returns:
        List[str]: list of requirements items

    CommandLine:
        python -c "import setup; print(setup.parse_requirements())"
    """
    import re
    import sys
    from os.path import exists
    require_fpath = fname

    def parse_line(line):
        """Parse information from a line in a requirements text file."""
        if line.startswith('-r '):
            # Allow specifying requirements in other files
            target = line.split(' ')[1]
            for info in parse_require_file(target):
                yield info
        else:
            info = {'line': line}
            if line.startswith('-e '):
                info['package'] = line.split('#egg=')[1]
            elif '@git+' in line:
                info['package'] = line
            else:
                # Remove versioning from the package
                pat = '(' + '|'.join(['>=', '==', '>']) + ')'
                parts = re.split(pat, line, maxsplit=1)
                parts = [p.strip() for p in parts]
                info['package'] = parts[0]
                if len(parts) > 1:
                    op, rest = parts[1:]
                    if ';' in rest:
                        version, platform_deps = map(str.strip,rest.split(';'))
                        info['platform_deps'] = platform_deps
                    else:
                        version = rest  # NOQA
                    info['version'] = (op, version)
            yield info

    def parse_require_file(fpath):
        with open(fpath, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    for info in parse_line(line):
                        yield info

    def gen_packages_items():
        if exists(require_fpath):
            for info in parse_require_file(require_fpath):
                parts = [info['package']]
                if with_version and 'version' in info:
                    parts.extend(info['version'])
                if not sys.version.startswith('3.4'):
                    # apparently package_deps are broken in 3.4
                    platform_deps = info.get('platform_deps')
                    if platform_deps is not None:
                        parts.append(';' + platform_deps)
                item = ''.join(parts)
                yield item

    packages = list(gen_packages_items())
    return packages

def getVersion(): # 获取版本号
    with open('FLite/version.py', 'r') as f:
        exec(compile(f.read(), 'FLite/version.py', 'exec'))
    return locals()['__version__']

def getReadme(): # 获取README.md文件
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    setup(
        name='FLite', # 包名
        version=getVersion(), # 版本号
        description='FLite is a federated learning framework for developers to quickly build federated learning applications.(Design and Implementation of a Topology Based Distributed Training Federated Learning Experimental Framework.)[Software Engineering, School of Computer Science and Technology, WUST, P. Qi(Sensorjang@wust.edu.cn)]',
        long_description=getReadme(), # 读取当前目录的README.md文件
        long_description_content_type='text/markdown', # 指定包文档格式为markdown
        author='P.Qi(Sensorjang)', # 作者
        author_email='Sensorjang@wust.edu.cn', # 作者邮箱
        keywords=['federated learning', 'machine learning', 'distributed machine learning', 'FL framework','privacy preserving'], # 关键字
        url='https://github.com/Sensorjang/FLite', # 项目主页
        download_url='https://github.com/Sensorjang/FLite.git', # 下载地址
        packages=find_packages(), # 自动查找包
        data_files=[('requirements', ['requirements/framework_environment.txt']), ('FLite', ['FLite/config.yaml'])], # 静态文件
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',
            # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Build Tools',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        license='MIT License', # 许可证
        install_requires=parse_requirements('requirements/framework_environment.txt'), # 自动安装依赖包
        extras_require={
            'all': parse_requirements('requirements.txt'),
        }, # 其他依赖包，需要手动安装
        ext_modules=[], # 扩展模块
        zip_safe=False # 是否压缩
    )