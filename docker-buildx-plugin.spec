Name: docker-buildx-plugin
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Docker buildx plugin (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/buildx-loong64
BugURL: https://github.com/kubernetes-loong64/buildx-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
Docker buildx plugin binary for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# No build step - pre-compiled binary

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 buildx %{buildroot}/usr/bin/docker-buildx

mkdir -p %{buildroot}/usr/libexec/docker/cli-plugins
install -m 755 buildx %{buildroot}/usr/libexec/docker/cli-plugins/docker-buildx

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/docker-buildx
/usr/libexec/docker/cli-plugins/docker-buildx

%changelog
