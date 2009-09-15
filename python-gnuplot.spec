Summary: A Python interface to the gnuplot plotting program
Name:    python-gnuplot
Version: 1.8
Release: %mkrel 3
Source0: http://downloads.sourceforge.net/gnuplot-py/gnuplot-py-%{version}.tar.gz
License: LGPLv2
Group:   Development/Python
Url:     http://gnuplot-py.sourceforge.net
Requires: gnuplot
Requires: python-numpy
Provides: gnuplot-py = %{version}
Buildrequires: python-devel
Buildrequires: gnuplot
Buildrequires: python-numpy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
Gnuplot.py is a Python package that interfaces to gnuplot,
the popular open-source plotting program. It allows you
to use gnuplot from within Python to plot arrays of data
from memory, data files, or mathematical functions.
If you use Python to perform computations or as 'glue'
for numerical programs, you can use this package to plot
data on the fly as they are computed. And the combination
with Python makes it is easy to automate things, including
to create crude 'animations' by plotting different datasets
one after another.
The package includes a demonstration that can be run by 
typing 'python %{py_puresitedir}/Gnuplot/demo.py'.

%prep
%setup -q -n gnuplot-py-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc ANNOUNCE.txt README.txt NEWS.txt FAQ.txt CREDITS.txt TODO.txt LICENSE.txt Gnuplot.html doc/
%{py_puresitedir}/*

