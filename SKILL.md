---
name: yc-design
description: YC 的个人IP设计系统。做HTML页面、个人网站、教程页面、介绍页面、landing page等任何前端设计时自动触发。包含品牌DNA和多个场景子规范。
---

触发条件：当用户要求制作HTML网页、个人页面、教程页面、介绍型页面、landing page、活动页面、App型页面、作品集等任何前端设计相关任务时触发。也在用户说"做图文"、"图文卡片"、"小红书图文"、"文章转卡片"、"转成图文"、"做卡片"时触发。

## 使用方式（7步工作流）

### Step 1: 澄清需求
向用户确认5个问题：
1. **类型** — 教程/介绍/科普？活动页/Landing？App型/功能型？**图文卡片？**
2. **受众** — 给谁看的？技术水平？
3. **Section数** — 大概几屏内容？
4. **素材** — 有哪些文案/图片/数据？
5. **硬约束** — 必须包含什么？有没有合作品牌色？

### Step 2: 读规范
1. **必读** `brand-dna.md` — 确认品牌底层规范
2. 根据类型选读场景文件：
   - 教程型/介绍型/科普型 → `references/scene-tutorial.md`
   - **教学型（教懂零基础/讲透/系统学/课程/教学slide）** → `references/scene-teaching.md`（在 scene-tutorial 之上的教学法升级层）
   - 活动页/分享会/Landing → `references/scene-landing.md`
   - App型/功能型（看板/书架/Canvas） → `references/scene-app.md`
   - **图文卡片/小红书图文/文章转卡片** → `references/scene-cards.md`

### Step 3: 拷模板
从 `assets/` 选择对应模板作为起点：
- 教程型 → `assets/template-tutorial.html`
- 活动页/Landing → `assets/template-landing.html`
- App型/功能型 → `assets/template-app.html`
- **图文卡片** → `assets/template-cards.html`

**从模板开始改，不从零写。**

### Step 4: 选布局组合
从 `references/layouts.md` 中选取 3~5 种布局模式，为每个 section 分配不同布局。

**每个 section 布局必须不同。**

（图文卡片模式：参考 `scene-cards.md` 中的推荐排版手法，为每页选择不同手法。）

### Step 5: 选组件填充
从 `references/components.md` 中选取组件填入各 section。

**硬规则：禁止使用任何HTML默认样式。** 所有引用块、列表、表格、卡片必须从 components.md 里选用对应组件的代码。不允许用默认 `<blockquote>`、默认 `border-left` 引用、无样式 `<ul>/<ol>`、默认 `<table>`。如果在 components.md 里找不到合适的，自己设计一个符合 brand-dna 规范的，但绝不能用浏览器默认样式。

### Step 6: 自检
对照 `references/checklist.md` 逐条检查：
- **P0 必须全过** — 任何一条不过就要改
- P1 应过 — 尽量满足
- P2 加分 — 锦上添花

（图文卡片模式：额外对照 `scene-cards.md` 底部的 Checklist。）

### Step 7: 交付
输出最终 HTML 文件，确保可直接在浏览器打开。

## IP 贴纸装饰（调用 yc-ip）

页面/卡片需要 YC 形象做装饰或辅助讲解时，**不要自己画、也不要只用通用 emoji**——用 YC 的 IP 贴纸，保证形象一致（红发 + 透明圆框眼镜 + chibi）。两条路径：

### 路径 A：复用现成贴纸（最快）
yc-ip 已有一套成品贴纸，直接拷来用：
- 来源：`~/.claude/skills/yc-ip/assets/examples/sticker/`（或桌面源 `YC_IP/yc-ip/assets/examples/sticker/`）
- 现成姿势：站姿叉袋 / 背包 / 坐姿用电脑 / 伏案记笔记 / 拿笑脸杯 / 戴耳机敲键盘 / 思考(带AI气泡) / 坐着看书
- 它们是 **418×418 纯白底**，必须先抠白底（见下方），再放进页面

### 路径 B：按当前任务现生成新贴纸（推荐，贴合内容）
当现成姿势都不贴合当前内容时，**调用 yc-ip 用 Sticker 模式生成一张新贴纸**：
1. 想清楚这一屏需要 YC 在「做什么动作 / 拿什么物件」来呼应该 section 的主题（例：讲"训练模型"→ YC 手摇一台小机器；讲"过拟合"→ YC 对着一张画得太满的纸皱眉）。
2. 按 yc-ip 的 **Sticker / Minimal** 规范生成：水彩铅笔轻手绘、**纯白 #FFFFFF 底**、单角色 + 一个动作/物件、0–3 个中文短词、比例多用 `1:1`。
3. 生图时固定附 yc-ip 的 canonical 锁图 `~/.claude/skills/yc-ip/assets/examples/sticker/00-reference-sheet-watercolor.png`（画风/长相锁），形象不稳再加 `character-reference/`。
4. 角色命脉：**红发 + 透明圆框眼镜 + chibi 缺一不可**。详规见 yc-ip 的 `references/prompt-template.md`、`style-dna.md`、`yc-character.md`。

> 注：实际生图依赖运行环境的 `image_gen` 工具；若当前环境无该工具，退化为路径 A（复用现成贴纸）。

### 铁律：每个位置按内容生成，不要全篇复用同一张
有 `image_gen` 时，**每个 section / 每张卡的 IP 图都要按该处内容单独生成一张新图**，动作和道具呼应当前这一段在讲什么——**禁止全篇只用同一张、或同几张不变的老贴纸糊上去**（那样会显得敷衍、像贴纸而非"老师在讲这一段"）。
- 复用 `assets/stickers/` 里的现成贴纸**只是无 image_gen 时的占位 fallback**，不是目标状态。
- 实现约定：在页面里给每个 IP 位置留一个**槽位说明**（如 `data-ip-slot="这张该画成什么"`，或集中成一个 `IP_SLOTS` 清单），写清该位置应生成的画面；占位先用现成贴纸，等到能生图时按槽位说明逐个替换成新图。参考 `examples/ml-teaching.html` 底部的 `IP_SLOTS` 写法。

### 抠白底 → 透明（A、B 都要做）
纯白底贴到奶白页面会露白方块。用内置脚本把白底抠透明（保留角色内部白衬衫/白鞋，不punch洞）：
```
python3 assets/sticker-cutout.py 输入.png 输出.png      # 单张
python3 assets/sticker-cutout.py /路径/raw-stickers/    # 整个文件夹 → cutout/
```
透明 PNG 统一存到 `assets/stickers/`，页面用相对路径引用。

### 放置规则（遵守 brand-dna 禁忌）
- **正放，禁止 rotate/歪斜**（brand-dna 明确禁忌）
- **克制**：一般每 1–2 屏最多 1 张，整页别堆贴纸
- 加 `drop-shadow` 让它"浮"在页面上；旁边可配 `Caveat` 手写体短批注做辅助讲解
- 移动端可缩小或隐藏贴纸（装饰非正文），但**不隐藏正文内容**

## 场景类型速查

| 类型 | 场景文件 | 模板 |
|------|----------|------|
| 教程型/介绍型/科普型 | `references/scene-tutorial.md` | `assets/template-tutorial.html` |
| 教学型/讲透/零基础/课程 | `references/scene-teaching.md`（+ scene-tutorial） | `assets/template-tutorial.html` |
| 活动页/分享会/Landing | `references/scene-landing.md` | `assets/template-landing.html` |
| App型/功能型 | `references/scene-app.md` | `assets/template-app.html` |
| 图文卡片/小红书图文 | `references/scene-cards.md` | `assets/template-cards.html` |

### 科普 vs 教学：别混了
"介绍/科普"目标是**让人感兴趣、有印象**（scene-tutorial）；"教学"目标是**让完全不懂的人彻底学会、能自己推理新情况**（scene-teaching，深度更高、有贯穿例子+检查理解+术语表）。触发词含 教程/讲透/零基础/系统学/课程/teach/lesson/教学slide → 升级到教学模式。拿不准就问用户："想让人感兴趣，还是真的学会？"

## 关键原则
- **从模板开始改，不从零写** — 模板已内置品牌变量和基础结构
- **每个 section 布局必须不同** — 避免单调重复，从 layouts.md 选不同模式
- **做完必须跑 checklist** — P0 全过才能交付

## 禁忌
严格遵守 `brand-dna.md` 的禁忌清单，不在此重复。核心底线：截图发 Twitter 不会被说"又是AI做的"。
