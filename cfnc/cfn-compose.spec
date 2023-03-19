Name:           cfnc
Release:        beta%{dist}
Version:        0.0.3
Summary:        A command-line tool for managing CloudFormation Stacks at scale.
BuildArch:      x86_64

License:        GPL
URL:            https://github.com/rbalman/cfn-compose
Source0:        https://github.com/rbalman/cfn-compose/archive/refs/tags/v0.0.3-beta.tar.gz

%description
A command-line tool for managing CloudFormation Stacks at scale.

%prep
%setup -q -n cfn-compose-%{version}-beta

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
make build
cp cfnc $RPM_BUILD_ROOT/usr/local/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/bin/cfnc

%changelog
* Sat Mar 18 2023 Yadav Lamichhane <omegazyadav1@gmail.com>
- Refactor sub commands of config command

