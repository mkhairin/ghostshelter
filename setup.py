from setuptools import setup, find_packages

setup(
    name='Ghostshelter',  # Nama paket Anda
    version='0.1',  # Versi paket Anda
    author='Muhammad Khairin',  # Nama Anda
    author_email='mkhairin04@gmail.com',  # Alamat email Anda
    description='A network scanning and analysis tool.',  # Deskripsi paket
    long_description=open('README.md').read(),  # Membaca deskripsi panjang dari README.md
    long_description_content_type='text/markdown',  # Jenis konten deskripsi panjang
    url='https://github.com/username/NetworkTool',  # URL repositori
    packages=find_packages(),  # Menemukan semua paket
    install_requires=[  # Daftar dependensi yang diperlukan
        'requests',
        'beautifulsoup4',
        'python-whois',
        'colorama',
    ],
    classifiers=[  # Klasifikasi paket
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versi Python yang dibutuhkan
)
