Summary: A Python interface to the gnuplot plotting program
Name:    python-gnuplot
Version: 1.8
Release: 4
Source0: http://downloads.sourceforge.net/gnuplot-py/gnuplot-py-%{version}.tar.gz
License: LGPLv2
Group:   Development/Python
Url:     http://gnuplot-py.sourceforge.net
Requires: gnuplot
Requires: python-numpy
Provides: gnuplot-py = %{version}
BuildRequires: python-devel
BuildRequires: gnuplot
BuildRequires: python-numpy
BuildRequires: pkgconfig(lapack)
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
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%files 
%doc ANNOUNCE.txt README.txt NEWS.txt FAQ.txt CREDITS.txt TODO.txt LICENSE.txt Gnuplot.html doc/
%{py_puresitedir}/*



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.8-3mdv2010.0
+ Revision: 442141
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.8-2mdv2009.1
+ Revision: 323716
- rebuild

* Wed Sep 03 2008 Gaëtan Lehmann <glehmann@mandriva.org> 1.8-1mdv2009.0
+ Revision: 279735
- import python-gnuplot


