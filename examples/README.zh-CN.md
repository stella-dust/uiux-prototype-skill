# 产品 UI 案例

[English](README.md) · [返回 skill 说明](../README.zh-CN.md)

这三个原创案例实际使用了 skill 的研究、委托选风格、完整原型和检查流程。各自 v0.1.0 是已封版的本地演示快照，manifest 保留本次风格委托记录，其授权不延伸到未来其他操作。

| 案例 | 主要流程 | 文件 |
|---|---|---|
| **Roam** | 发现旅行、查看行程、收藏与恢复空状态 | [原型](roam-mobile/docs/prototype/versions/v0.1.0/mobile/index.html) · [风格研究](roam-mobile/docs/prototype/versions/v0.1.0/style-reference.html) · [规范](roam-mobile/docs/prototype/versions/v0.1.0/design-system.html) · [DESIGN.md](roam-mobile/docs/prototype/versions/v0.1.0/DESIGN.md) · [QA](roam-mobile/docs/prototype/versions/v0.1.0/QA.md) |
| **Pulse** | 项目与产能概览、筛选、新建校验和详情 | [原型](pulse-web/docs/prototype/versions/v0.1.0/web/index.html) · [风格研究](pulse-web/docs/prototype/versions/v0.1.0/style-reference.html) · [规范](pulse-web/docs/prototype/versions/v0.1.0/design-system.html) · [DESIGN.md](pulse-web/docs/prototype/versions/v0.1.0/DESIGN.md) · [QA](pulse-web/docs/prototype/versions/v0.1.0/QA.md) |
| **Arc Library** | 素材与集合、搜索、视图切换、检查器和键盘预览 | [原型](arc-desktop/docs/prototype/versions/v0.1.0/desktop/index.html) · [风格研究](arc-desktop/docs/prototype/versions/v0.1.0/style-reference.html) · [规范](arc-desktop/docs/prototype/versions/v0.1.0/design-system.html) · [DESIGN.md](arc-desktop/docs/prototype/versions/v0.1.0/DESIGN.md) · [QA](arc-desktop/docs/prototype/versions/v0.1.0/QA.md) |

## 本地运行

在仓库根目录运行：

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

打开[案例总览](http://localhost:8765/examples/)。原型使用浏览器本地状态，没有生产后端。[总览 HTML 源码](index.html)。

## 来源与验证范围

各 `references.json` 保留 Dribbble 来源和实际查看范围，没有打包参考作品图。界面代码与 SVG 图形为原创；Roam 的生成海岸图附有来源记录。地点、项目、文件大小等内容是演示数据。浏览器检查不等同于原生 SDK、设备、后端或完整无障碍验收，具体范围见各 QA 文件。

案例封版目录逐字节复制，manifest 指纹保持有效；导航和 README 配图放在快照目录之外。原创文件沿用仓库的 [MIT 许可](../LICENSE)。
