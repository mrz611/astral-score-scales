# 第三方来源说明

本项目的回放解析模块和数据文件来自：

- 项目：AstralParty_Dex（星趴档案）
- 作者：Nemophila & ZtyanCrany
- 来源：https://github.com/ZtyanCrany/AstralParty_Dex
- 许可证：MIT
- 固定源码版本：`e204900e41389a47310edccc11778812e93a52a1`

保留的内容：

- `astral/`：`review.py`、`replay.py`、`proto_loader.py`、`paths.py`、`log.py` 及包入口。
- `assets/proto/`：回放解析所需的 protobuf 描述符。
- `assets/data/`：解析及角色名称所需的少量 JSON 数据表。

原项目的 MIT 许可证完整保留在 `THIRD_PARTY_LICENSES/AstralParty_Dex.LICENSE`。

本项目未引入原项目的登录、界面、账号、签名密钥、用户数据或美术资源。`rate_core.py` 是回放下载、特征整理和 v0.2 量表评分的独立适配层。
