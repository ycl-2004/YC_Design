# YC Design

YC Design 是 YC 的个人品牌设计与前端交付系统。它把内容意图、品牌规则、场景方法、组件、YC-IP 图像和自动 QA 串成一条可执行工作流。

它不是“按一个按钮生成同一种页面”。它的目标是：**在不同用途和视觉语气下仍然像 YC，同时不落入通用 AI 模板。**

## 能做什么

| Scene | 目标 | 输出 |
|---|---|---|
| Tutorial | 让人感兴趣、理解概念 | 编辑型滚动长页 |
| Teaching | 让零基础真正学会并能推理 | 贯穿案例、互动、测验、术语表 |
| Landing | 建立期待并促成行动 | 活动/产品报名页 |
| App | 快速操作、扫描状态 | 看板、书架、工具页 |
| Cards | 移动端传播 | 1080x1440 多卡片与本地导出 |

## 系统结构

```text
SKILL.md                         工作流与路由
brand-dna.md                     唯一品牌真源与规则优先级
references/visual-modes.md       editorial / technical / quiet / conversion
references/scene-*.md            五种场景方法
references/components/catalog.json 组件元数据与准入状态
references/components.md         legacy code cookbook（按需读取）
assets/template-*.html           五个独立起手模板
assets/ip-manifest.json          YC-IP 资产登记
examples/*.html                  可运行成品
scripts/qa-*                     静态与视觉 QA
```

## 品牌核心

- 酒红 `#B23A48` / 深酒红 `#8E2C3A`：YC、主判断、主行动
- 牛仔蓝 `#3B6EA5` / 深蓝 `#346294` / 浅蓝 `#9DBDE0`：技术、系统、连接，并保证浅底/深底可读
- 软粉 `#CB5A78` / 深粉 `#9F3754`：情感与提醒；软粉只作点睛，可读文字用深粉
- 暖奶白环境、墨色正文、衬线标题与无衬线正文
- YC 角色固定为酒红乱发、透明圆框眼镜、chibi 比例

颜色比例是语义权重，不是像素面积。页面也不需要同时出现虚线圆、Caveat、巨型标题和贴纸；每页只选 2-4 个签名元素。

## 四种视觉语气

- `editorial`：内容与观点，强调排版叙事
- `technical`：功能与系统，强调密度、状态和反馈
- `quiet`：作者与长文，强调留白和信任
- `conversion`：活动与发布，强调节奏、证据和行动

同一品牌在不同任务里可以明显变化，但颜色语义、排版判断和 YC 人格保持一致。

## 使用

直接说：

```text
用 yc-design 把复利给零基础讲透，做成教学页。
用 yc-design 做一个 AI 分享会的报名 Landing。
把这篇文章转成 8 张 YC 小红书图文卡片。
```

信息足够时系统直接执行；只有关键缺口会导致做错时才提问。

## 本地运行

```bash
cd YC_Design
python3 -m http.server 8765
```

打开 `http://localhost:8765/examples/` 下的页面。

## QA

```bash
npm run qa:static
npm run qa:visual
npm run qa
```

视觉 QA 会在 320、768、1280 三个宽度生成截图，并检查控制台错误、横向溢出、图片、对比度和关键交互。低对比可见文本是硬错误，不是人工 warning。

## 组件策略

`references/components/catalog.json` 是组件真源，包含：

- 适用 scene 与 visual mode
- 信息密度
- 是否交互
- 移动端策略
- 可访问性要求
- `approved / experimental / deprecated` 状态

`components.md` 保留完整代码片段，但不再允许 AI 从中随机挑选。先选 catalog，再读对应代码。

## YC-IP 资产

所有生成图必须进入 `assets/ip-manifest.json`，登记 slot、promptSummary、sourceImage、transparent、usedBy 和 status。主解释图按 yc-ip Sample / Standard 生成；轻贴纸仅在明确需要时使用。不同语义位置不复用同一张图。

## Credits

YC Design 由 YC 持续维护。早期结构基于 Esther 不二的开源设计系统模板改造，并受归藏 PPT Design Skill 启发；当前品牌规则、视觉模式、教学系统、YC-IP 工作流和 QA 已形成 YC 自有标准。

## 版权 · License

© 2026 Yi-Chen Lin（林羿辰 / **YC**）。**保留一切权利 / All Rights Reserved.**

本仓库为 YC 的个人作品，**版权归 YC 所有**。源码与素材公开仅供浏览与参考，**未经书面许可，不得复制、修改、再分发或用于商业用途**。YC 的品牌规则、视觉模式与 YC-IP 资产为 YC 专有，**不在任何开源 / 共享授权范围内**（上文 Credits 中标注的第三方开源模板与灵感来源除外，其归属各自原作者）。

This is YC's personal work, public for viewing only — no copying, modifying,
redistribution, or commercial use without written permission. YC's brand rules,
visual modes, and YC-IP assets are proprietary and are **not** open-source or
shared (third-party open-source templates and inspirations noted in *Credits*
remain under their own licenses). See [LICENSE](LICENSE) · Contact:
yichen.lin.2004@gmail.com
