#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-distr
Version  : 2.8.0
Release  : 16
URL      : https://cran.r-project.org/src/contrib/distr_2.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/distr_2.8.0.tar.gz
Summary  : Object Oriented Implementation of Distributions
Group    : Development/Tools
License  : LGPL-3.0
Requires: R-distr-lib = %{version}-%{release}
Requires: R-sfsmisc
Requires: R-startupmsg
BuildRequires : R-sfsmisc
BuildRequires : R-startupmsg
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-distr package.
Group: Libraries

%description lib
lib components for the R-distr package.


%prep
%setup -q -c -n distr
cd %{_builddir}/distr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589782413

%install
export SOURCE_DATE_EPOCH=1589782413
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library distr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library distr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library distr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/distr/ARITHMETICS
/usr/lib64/R/library/distr/CITATION
/usr/lib64/R/library/distr/DESCRIPTION
/usr/lib64/R/library/distr/INDEX
/usr/lib64/R/library/distr/MASKING
/usr/lib64/R/library/distr/Meta/Rd.rds
/usr/lib64/R/library/distr/Meta/demo.rds
/usr/lib64/R/library/distr/Meta/features.rds
/usr/lib64/R/library/distr/Meta/hsearch.rds
/usr/lib64/R/library/distr/Meta/links.rds
/usr/lib64/R/library/distr/Meta/nsInfo.rds
/usr/lib64/R/library/distr/Meta/package.rds
/usr/lib64/R/library/distr/Meta/vignette.rds
/usr/lib64/R/library/distr/NAMESPACE
/usr/lib64/R/library/distr/NEWS
/usr/lib64/R/library/distr/R/distr
/usr/lib64/R/library/distr/R/distr.rdb
/usr/lib64/R/library/distr/R/distr.rdx
/usr/lib64/R/library/distr/TOBEDONE
/usr/lib64/R/library/distr/demo/ComparisonFFTandRtoDPQ.R
/usr/lib64/R/library/distr/demo/ConvolutionNormalDistr.R
/usr/lib64/R/library/distr/demo/Expectation.R
/usr/lib64/R/library/distr/demo/NormApprox.R
/usr/lib64/R/library/distr/demo/StationaryRegressorDistr.R
/usr/lib64/R/library/distr/demo/destructive.R
/usr/lib64/R/library/distr/demo/nFoldConvolution.R
/usr/lib64/R/library/distr/demo/range.R
/usr/lib64/R/library/distr/doc/index.html
/usr/lib64/R/library/distr/doc/newDistributions-knitr.R
/usr/lib64/R/library/distr/doc/newDistributions-knitr.Rnw
/usr/lib64/R/library/distr/doc/newDistributions-knitr.pdf
/usr/lib64/R/library/distr/help/AnIndex
/usr/lib64/R/library/distr/help/aliases.rds
/usr/lib64/R/library/distr/help/distr.rdb
/usr/lib64/R/library/distr/help/distr.rdx
/usr/lib64/R/library/distr/help/paths.rds
/usr/lib64/R/library/distr/html/00Index.html
/usr/lib64/R/library/distr/html/R.css
/usr/lib64/R/library/distr/tests/Examples/distr-Ex_i386.Rout.save
/usr/lib64/R/library/distr/tests/Examples/distr-Ex_x64.Rout.save
/usr/lib64/R/library/distr/tests/doSvUnit.R
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunMinimum.R
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunMinimum.save
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunOperatorsMethods.R
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunOperatorsMethods.save
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunQQPlot.R
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunQQPlot1.save
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunQQPlot2.save
/usr/lib64/R/library/distr/tests/unitTests/runit.dontrunQQPlot3.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/distr/libs/distr.so
/usr/lib64/R/library/distr/libs/distr.so.avx2
/usr/lib64/R/library/distr/libs/distr.so.avx512
