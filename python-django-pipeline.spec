#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	An asset packaging library for Django
Name:		python-django-pipeline
Version:	1.2.21
Release:	2
License:	MIT
Group:		Applications/Networking
URL:		https://github.com/cyberdelia/django-pipeline
Source0:	http://pypi.python.org/packages/source/d/django-pipeline/django-pipeline-%{version}.tar.gz
# Source0-md5:	7915514e7cd5dcde0c9ad29d8cc58dba
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-django
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pipeline is an asset packaging library for Django, providing both CSS
and JavaScript concatenation and compression, built-in JavaScript
template support, and optional data-URI image and font embedding

%prep
%setup -q -n django-pipeline-%{version}
%{__rm} -r django_pipeline*.egg-info

%build
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

# Remove the "tests" subdirectory to avoid it polluting the main python namespace:
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE AUTHORS HISTORY.rst README.rst
%dir %{py_sitescriptdir}/pipeline
%dir %{py_sitescriptdir}/pipeline/compilers
%dir %{py_sitescriptdir}/pipeline/compressors
%dir %{py_sitescriptdir}/pipeline/conf
%dir %{py_sitescriptdir}/pipeline/jinja2
%dir %{py_sitescriptdir}/pipeline/templatetags
%{py_sitescriptdir}/pipeline/*.py[co]
%{py_sitescriptdir}/pipeline/compilers/*.py[co]
%{py_sitescriptdir}/pipeline/compressors/*.py[co]
%{py_sitescriptdir}/pipeline/conf/*.py[co]
%{py_sitescriptdir}/pipeline/jinja2/*.py[co]
%{py_sitescriptdir}/pipeline/templates
%{py_sitescriptdir}/pipeline/templatetags/*.py[co]
%{py_sitescriptdir}/django_pipeline*.egg-info

