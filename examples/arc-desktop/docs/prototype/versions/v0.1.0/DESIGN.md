# Arc Library — Design contract v0.1.0

日期：2026-11-04。对象：独立设计师、创意团队成员。场景：在桌面整理和查找品牌、编辑和动态素材。目标：在浏览集合、筛选、预览、检查和标记之间保持上下文，降低找图与交接成本。

## Direction and approval

选择 **Midnight Studio**。真实 Dribbble 图像研究与备选比较见 style-reference.html，详情见 references.json。用户当前明确授权风格选择：**“由你定风格，直接完成三个案例”**。先完成风格参考并以 helper 记录文件 SHA-256 和该原话，再 prepare 生成完整原型。没有将 HTML 预览按钮视作授权。

## Scope

仅桌面 App HTML 模拟。屏幕/路径：全素材网格、收藏、最近加入、三个分类集合；名称/标签搜索；类型筛选和排序；网格/列表切换；常驻/折叠检查器；大图 dialog；收藏、标签、创建集合、复制详情（含拒绝剪贴板后的手动退路）。12 件作品全部为本案例原创 SVG。

PNG/PDF 等文件名、尺寸、大小、日期、作者身份与存储概况是合成展示数据；实际提供的视觉文件是 SVG。没有原生文件访问、Finder、导入、账户、协作或后端连接。localStorage 保存本浏览器的收藏/标签/新集合，失败时保留会话内状态并提示。

## Tokens

唯一值源：assets/tokens.css。应用样式：assets/app.css；可视化规范引用同一 token 文件。

| role | exact value | use |
|---|---|---|
| bg | #111315 | 全局画布 |
| surface | #191C20 | 中央作品区 |
| raised | #23262B | 覆盖层/次级控件 |
| soft | #2A2E33 | 已选工具 |
| border | #2D3238 | 区域边界 |
| text | #EEF0ED | 主信息 |
| muted | #A0A7AF | 辅助信息 |
| dim | #717A85 | 非关键次级元数据 |
| accent | #D8FF6C | 主行动、选择、焦点 |
| accent-ink | #1B2410 | 亮按钮文字 |
| error | #FFA18F | 字段错误 |

字体：-apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, sans-serif；不下载第三方字体。应用标题25px/1.15、字距-0.8px、weight550；检查器标题14px/1.35；控件11–12px；元数据9–10px。token 为系统主色，作品内容可以有其原创配色。金额/可比较数值不截断；长名称用省略并在检查器完整换行。

间距：4、8、12、16、24、32px。常规边框1px；控件圆角5–6px，缩略图5px，dialog12px。普通表面不用装饰阴影；侧层/dialog 以投影分隔。

## Layout and platform

三栏：204px + minmax(0,1fr) + 284px；≥1640时220px + flexible +310px，作品四列；标准三列，1240以下两列；1020以下检查器折叠侧层，作品三列；800以下侧栏图标化，作品两列；580以下提供紧凑提示但保留操作。优先显示作品与选择信息，独立栏滚动，不能出现文档横向溢出。标题栏圆点为示意，非操作按钮。

## Interaction and state

导航即刻切换；筛选按名称、文件名和含用户标签搜索，分类支持SVG/PNG/PDF。收藏计数同步；创建集合必须输入非空、不可重名，自动加入当前选中作品；标签非空且不可重复。主要操作语义按钮；图像卡选择与收藏按钮互不嵌套。dialog 标题、关闭按钮和原生焦点行为完整。

状态入口：desktop/index.html?state=loading（1400ms本地骨架后完成）、?state=error（重试700ms本地恢复）、?state=empty（返回全素材）。无结果与初次空收藏给出明确返回操作。剪贴板拒绝时可在文本框选择复制；所有成功指的是本地状态。

键盘：/ 搜索、F 收藏、G 视图、Space 预览、Escape 关闭；文本输入、已开dialog、Ctrl/Meta/Alt组合键不拦截。Space 在按钮和链接保留原生行为。

## Motion

180ms cubic-bezier(.2,.8,.2,1)：缩略图悬停scale1.018，反馈toast opacity/translate；收藏淡显120ms。搜索/集合/视图即时，不动每行数据。prefers-reduced-motion取消位移/渐变与骨架动画，保留反馈。未使用layout-per-frame、全屏模糊或外部动画库。

## Verification and handoff

实际检查与未验证项见 QA.md。浏览器布局与本地交互不证明原生窗口、系统快捷键/权限、实机帧率或真实文件能力。后续实现优先复用成熟文件索引/数据库、宿主菜单、可访问组件。保留本快照，新增功能创建新版本，不能静默修改已封版材料。
