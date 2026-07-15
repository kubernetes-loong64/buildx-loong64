# Docker Buildx for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/Docker%20Buildx%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=docker&logoColor=white" alt="Docker Buildx LoongArch64 龙芯架构发行版"></p>

通过 CI/CD 构建 [Docker Buildx](https://github.com/docker/buildx) 的 **LoongArch64 (loong64)** 架构二进制文件。

## 工作原理

GitHub Actions 工作流克隆指定的 docker/buildx 版本，使用 `GOOS=linux GOARCH=loong64` 交叉编译，并上传构建产物作为
工作流产物。目标平台：`linux/loong64`。

## 分支命名

推送 `loong64-buildx-v<版本>` 格式的分支（如 `loong64-buildx-v0.30.1`）即可触发构建。可追加 `+<build>`
（如 `loong64-buildx-v0.30.1+0`）携带构建元数据。

## [发布](https://github.com/kubernetes-loong64/buildx-loong64/releases)

推送 `release-loong64-buildx-v<版本>` 格式的标签（如 `release-loong64-buildx-v0.30.1+0`）即可自动创建 GitHub
Release 并上传构建产物。

`+<build>` 后缀提供构建元数据（如 `+0`、`+1-alpha.1`）。

后缀表示发布阶段：

| 后缀      | 阶段   |
|---------|------|
| `alpha` | 内测版  |
| `beta`  | 公测版  |
| `rc`    | 预发布版 |
| （无后缀）   | 正式版  |

## 发布产物

每个发布包含以下文件：

| 文件       | 描述                  |
|----------|---------------------|
| `buildx` | Docker Buildx 二进制文件 |

每个文件都有对应的 `.asc` 分离式 GPG 签名。

## 验证发布

- 发布文件使用 GPG 签名。
- 从 [keys.openpgp.org](https://keys.openpgp.org) 下载公钥。
- 指纹：[FCF8724722CCBF9F51B1FBE376532BE7E3013105](https://keys.openpgp.org/debug?q=FCF8724722CCBF9F51B1FBE376532BE7E3013105)
- [手动下载](https://keys.openpgp.org/vks/v1/by-fingerprint/FCF8724722CCBF9F51B1FBE376532BE7E3013105)

```shell
gpg --keyserver keys.openpgp.org --recv-keys FCF8724722CCBF9F51B1FBE376532BE7E3013105
echo "FCF8724722CCBF9F51B1FBE376532BE7E3013105:6:" | gpg --import-ownertrust
```

或者，手动下载公钥文件后导入：

```shell
gpg --import /tmp/xxx
```

每个发布产物都有对应的 `.asc` 分离式签名。要验证，请从发布页面下载文件和其对应的 `.asc` 签名，然后执行：

```shell
gpg --verify <文件>.asc <文件>
```

## 参考仓库

- [src-anolis-os/docker](https://gitee.com/src-anolis-os/docker)

## 文档

> 适用于：moby-loong64、tini-loong64、cli-loong64、runc-loong64、containerd-loong64

- [Install containerd and docker binaries on LoongArch](https://xuxiaowei.io/t/754)
- [Install containerd and docker RPM packages on LoongArch](https://xuxiaowei.io/t/811)

## 许可证

[Apache License 2.0](LICENSE)
