# AI Native Factory V1 Architecture and Action Program Design

日期：2026-05-06  
状态：Design draft for review  
定位：独立规格文档；本文吸收并重构既有 AI 原生工厂、加工智能体、对象模型、子系统设计和图片计划中的有效信息，但阅读和实施不依赖原始五份初稿。

## 1. 一句话定义

AI Native Factory V1 是一个面向真实物理产线的工业操作系统原型。它以工序/装夹级 Operation Execution Package 为系统事实主轴，以对象服务、作业包服务、事件总线和 Agent Runtime 为最小工业操作内核，以 Agent 工作流实现 DFM/报价、工艺路线和资源选择建议，以 Machine Physical Agent 给加工设备安装感知器官、边缘大脑、反射回路和受控执行接口。

V1 不是传统 MES 加几个 Copilot，也不是一堆 Agent 互相聊天。它的目标是让真实订单从图纸进入，到预算级报价、DFM、工艺/CAPP/CAM、作业包、仿真/审批、验证机受控执行、质量/异常回写、知识沉淀，形成一条可采纳、可解释、可审计、可复盘、可扩展到 20 台加工设备的闭环。

## 2. 核心设计判断

### 2.1 不推翻原有思路，但重排主线

既有初稿中最有价值的主线是：

- 作业包作为执行组织方式。
- 对象模型和事件作为多 Agent 协同底座。
- 成熟工业硬件 + 自研 AI Agent + 边缘闭环控制。
- 安全门和人工审批作为工业可信边界。
- 加工设备、刀具、夹具、质量、物流等对象可计算、可追溯。

需要批判性修正的是：

- V1 边界过大，容易把平台操作系统、Agent 工作流、20 台物理产线、机器人自动化、自适应控制、本体和知识学习一次性混在一起。
- 作业包概念还不够硬，必须从“资料包”升级为“可放行、可执行、可审计、可回写的工业执行契约”。
- 物理 Agent 不能只是数据采集网关，应是软硬件一体的 cyber-physical agent。
- Agent 不能成为生产事实主轴，否则系统容易退化成不可治理的工作流平台。

### 2.2 正式主路线

采用“作业包操作系统主线”：

- Operation Execution Package 是事实主轴。
- Agent Runtime 是智能入口。
- Machine Physical Agent 是物理执行与感知载体。
- 20 台产线是 V1 建设目标，但第一实践阶段从 1 台验证机打穿生产级首单闭环开始。

用一句话约束架构：

**Agent 很聪明，但作业包说了算；物理 Agent 会行动，但执行事实必须回写作业包。**

## 3. V1 范围

### 3.1 V1 做什么

V1 同时推进三条轨道：

1. OEP 操作内核：对象服务、作业包服务、事件总线、Agent Runtime。
2. Agent 工作流：DFM/报价、工艺路线、刀具/夹具/机床选择、OEP 生成与 Gate 检查。
3. 物理 Agent / 产线硬件：第一台验证机的感知器官、边缘大脑、反射回路、OEP 接口，并为 20 台产线复制预留标准化规格。

第一实践阶段的真实场景：

- 真实历史订单。
- 零件以简单板块、支架、治具、简单壳体为主，允许少量接近中等复杂度。
- 1 台验证机。
- 人工辅助物流、装夹、刀具准备、质检。
- 系统拥有记录权、建议权、放行权和人审后的受控执行权。

### 3.2 V1 暂不追求什么

- 不追求全品类工艺自动生成。
- 不让 AI 自动修改 NC 并直接执行。
- 不从第一天实现 20 台设备完整动态调度。
- 不在第一实践阶段开放 Feed Override 闭环控制。
- 不做完整 ERP/MES/WMS/QMS 替代。
- 不做全量 OWL 本体，先用受控词表、结构化规则表、工艺模板库和可查询对象关系。

## 4. 最小工业操作内核

V1 内核由四个产品级组件组成。它们必须服务于 OEP，而不是各自成为孤岛。

### 4.1 对象服务

职责：

- 管理对象、版本、状态、关系和附件。
- 为 Agent、OEP、事件、HMI、物理 Agent 提供统一事实来源。

V1 必须覆盖的对象：

| 域 | 对象 |
|---|---|
| 商务 | CustomerOrder, Quotation |
| 工程 | Part, Drawing, CADModel, ManufacturingFeature |
| 工艺 | ProcessPlan, Operation, SetupPlan, Toolpath, NCProgram |
| 执行 | OperationExecutionPackage, ExecutionRecord, Event, Exception |
| 资源 | Machine, WorkCenter, Operator |
| 工装 | ToolAssembly, Fixture, Pallet |
| 物料 | MaterialLot, Inventory, StorageLocation |
| 质量 | InspectionPlan, MeasurementResult, QualityEvent |
| 智能 | Agent, Decision, KnowledgeItem, Model |

对象服务边界：

- 不直接编排流程。
- 不直接调用设备。
- 不进行 Agent 推理。
- 不把历史记录静默覆盖，关键对象必须版本化。

### 4.2 作业包服务

职责：

- 管理 Operation Execution Package 的 schema、生命周期、安全门、审批、发布、暂停、回写和归档。
- 将工艺、资源、程序、质量、安全门和执行记录组织成一个可执行生产事实。

V1 的 OEP 采用三段结构：

- Plan：计划事实。
- Gate：放行事实。
- Trace：执行事实。

### 4.3 事件总线

职责：

- 记录和分发对象状态变化、OEP 生命周期变化、审批、异常和执行回写。
- 支持幂等、可追溯、关键事件持久化和重放。

事件是已发生事实，不是命令。命令可以由 Agent、HMI 或服务发起，但命令结果必须回写为事件。

事件 envelope：

```json
{
  "event_id": "EVT-20260506-000001",
  "event_type": "OEP.GateChecked",
  "source": "machine-physical-agent",
  "subject": "OEP-20260506-0001",
  "time": "2026-05-06T10:30:00+08:00",
  "schema_version": "1.0",
  "correlation_id": "CORR-SO-00088",
  "causation_id": "EVT-20260506-000000",
  "actor": {
    "type": "agent",
    "id": "PACKAGE_GATE_AGENT"
  },
  "payload": {
    "gate": "tool_life",
    "status": "passed",
    "evidence_ref": "decision://DEC-000921"
  }
}
```

### 4.4 Agent Runtime

职责：

- 运行决策 Agent。
- 管理 Agent 合同、工具注册、权限、风险等级、审批和决策日志。
- 强制 Agent 输出结构化建议、依据、风险、受影响对象、审批需求和采纳状态。

Agent Runtime 边界：

- Agent 不能绕过对象服务传递隐含状态。
- Agent 不能绕过 OEP 放行。
- Agent 不能直接执行高风险物理动作。
- Agent 的关键输出必须形成 DecisionLog。

## 5. Operation Execution Package 定义

### 5.1 作业包层级

作业包不是一个层级扁平的“大文件夹”，而是一组有层级的工业执行契约。

| 层级 | 名称 | 作用 | 是否直接执行 |
|---|---|---|---|
| L0 | Order Mission Package | 客户订单或项目级任务包，表达交付目标、商业约束和优先级 | 否 |
| L1 | Part Lot Package | 某零件某批次制造包，承接图纸、CAD、工艺路线、质量要求和批次追溯 | 否 |
| L2 | Operation Execution Package | 一次工序/装夹/机床执行的放行单位 | 是 |
| L3 | Auxiliary Execution Package | 刀具准备、夹具准备、搬运、检测等附属任务 | 间接执行 |

V1 产品级实现 L2 Operation Execution Package。L0/L1 先作为聚合视图和追溯结构存在。

### 5.2 OEP 最小内容

OEP 必须包含五类内容：

- 工程上下文：订单、零件、图纸/CAD 版本、工序、装夹。
- 执行资源：机床、NC 程序、刀具组件、夹具/托盘、操作员。
- 质量要求：关键尺寸、测量计划、首件/末件/抽检要求。
- 安全门：仿真结果、刀具寿命、装夹确认、权限审批。
- 执行回写：开始/结束、暂停、报警、测量结果、异常、最终判定。

### 5.3 Plan / Gate / Trace schema

内部机器形态采用 JSON Schema / API，人工界面渲染为作业卡和审批表单。

```json
{
  "package_id": "OEP-20260506-0001",
  "package_type": "OperationExecutionPackage",
  "status": "ReadyForApproval",
  "parent_refs": {
    "order_mission_package_id": "OMP-SO-00088",
    "part_lot_package_id": "PLP-PART-BRACKET-001-LOT01"
  },
  "plan": {
    "order_ref": {
      "customer_order_id": "SO-00088",
      "quotation_id": "QUO-00088-V2"
    },
    "part_ref": {
      "part_id": "PART-BRACKET-001",
      "drawing_id": "DWG-BRACKET-001-A3",
      "cad_model_id": "CAD-BRACKET-001-A3"
    },
    "operation_ref": {
      "process_plan_id": "PP-BRACKET-001-V1",
      "operation_id": "OP20-FINISH",
      "setup_plan_id": "SETUP-OP20-A",
      "nc_program_id": "NC-OP20-V4"
    },
    "resources": {
      "machine_id": "MC-5AX-001",
      "tool_assembly_ids": ["TASM-D10-0001", "TASM-D6-0007"],
      "fixture_id": "FIX-ZP-320-001",
      "pallet_id": "PALLET-0007",
      "operator_skill_required": ["5axis_setup", "first_article_approval"]
    },
    "quality": {
      "inspection_plan_id": "IP-BRACKET-OP20",
      "critical_characteristics": ["DATUM_A", "HOLE_PATTERN_01", "FLATNESS_A"]
    }
  },
  "gate": {
    "engineering_version_consistency": "passed",
    "resource_kitting": "passed",
    "tool_life": "passed",
    "fixture_and_pallet_confirmed": "pending",
    "simulation": "passed",
    "quality_plan_ready": "passed",
    "authority_approval": "required"
  },
  "trace": {
    "execution_records": [],
    "measurement_results": [],
    "exceptions": [],
    "decision_log_refs": []
  }
}
```

### 5.4 生命周期

```text
Draft
  -> EngineeringReady
  -> ResourceChecked
  -> Simulated
  -> Approved
  -> Released
  -> Staged
  -> Executing
  -> Paused
  -> Completed
  -> Archived
```

允许异常回路：

- `Paused -> Executing`
- `Paused -> ReworkRequired`
- `ReworkRequired -> Draft`
- `Released -> Cancelled`

### 5.5 放行门

V1 OEP 发布前至少通过：

| Gate | 检查内容 | 失败处理 |
|---|---|---|
| Engineering Gate | 图纸、CAD、工艺、NC 版本一致 | 返回工程修改 |
| Resource Gate | 机床、刀具、夹具、人员可用 | 触发齐套/替代建议 |
| Tool Gate | 刀具组件身份、寿命、几何、刀补可用 | 锁定或替代 |
| Fixture Gate | 夹具/托盘匹配、装夹确认、干涉风险 | 阻断并请求确认 |
| Simulation Gate | CAM/机床/夹具/机器人相关仿真或检查结果 | 返回方案修改 |
| Quality Gate | 检测计划、关键尺寸、测量方法明确 | 阻断发布 |
| Authority Gate | 审批权限、风险等级、人审记录齐全 | 请求审批 |

放行强度分阶段：

1. 流程放行：系统不批准，不生成正式 OEP；人可绕过，但绕行记录为例外。
2. 系统放行：系统不批准，不能通过 HMI/MES 下发任务；CNC 本机仍保留应急人工操作。
3. 局部技术互锁：成熟后对刀具身份、装夹确认、程序版本等高风险点做 PLC/CNC 局部互锁。

## 6. Agent 工作流

V1 先实现四个核心决策 Agent。

### 6.1 Intake / DFM / Quote Agent

职责：

- 解析订单、图纸、CAD 和历史信息。
- 输出 DFM 风险、报价假设、预算级报价建议和交期风险。
- 将报价建议拆分为材料、工时、机时、刀具、夹具、风险缓冲和交期假设。

边界：

- V1 做预算级报价，生产使用逐步逼近承诺级。
- 正式报价承诺必须人审、版本化、可追溯。
- Agent 推理只做解释和补充建议，不直接作为价格权威。

报价模型：

- 工艺模板 + 标准工时 + 材料/刀具/机时单价作为底座。
- 历史相似订单作为校准。
- Agent 负责解释、风险提示和补充建议。

### 6.2 Process Agent

职责：

- 基于工艺模板、结构化规则和工艺员输入，生成或补全工艺路线。
- 生成装夹方案、刀具/夹具/机床选择建议、CAM/NC 任务。
- 标记工艺风险、替代方案和需要人工确认的内容。

边界：

- 不要求 V1 全自动 CAPP/CAM。
- 工艺员是系统的一部分，人工补全和修改必须形成结构化 diff。
- 不能直接修改已批准工艺，不能绕过审批生成执行态 NC。

### 6.3 Package / Gate Agent

职责：

- 从对象、工艺、资源和质量要求生成 OEP 草案。
- 检查工程版本、资源齐套、仿真结果、刀具寿命、夹具确认和审批条件。
- 提出放行、阻断或补齐建议。

边界：

- 可以建议阻断或放行，但最终放行由作业包服务和审批策略执行。
- 不能用自然语言解释替代结构化 Gate 结果。

### 6.4 Execution / Trace Agent

职责：

- 解释执行状态、报警、测量结果和异常。
- 生成追溯报告、复盘建议和下一单改进建议。

边界：

- V1 不以它作为最强智能卖点。
- 先保留基础追溯和解释能力。
- 执行/质量复盘在后续版本增强。

### 6.5 V1 智能价值排序

V1 最需要证明 Agent 价值的建议类型：

1. DFM/报价建议。
2. 工艺路线建议。
3. 刀具/夹具/机床选择建议。

安全门/放行建议、执行/质量复盘建议也很核心，但作为后续版本增强。

### 6.6 知识基础

长期知识来源包括：

- 历史订单、报价、工艺、质量记录。
- 工艺员专家规则和人工维护工艺模板。
- 刀具、夹具、机床、材料等结构化主数据。
- 外部供应商资料、标准和手册。
- 首单执行后形成的新案例库。

V1 实践以工艺员专家规则和工艺模板为主。知识表达采用三层：

| 层 | 形式 | 作用 |
|---|---|---|
| 解释层 | 文档/RAG | 说明为什么 |
| 约束层 | 结构化规则表 | 校验能不能 |
| 生成层 | 工艺模板库 | 生成初稿 |

所有 Agent 建议必须记录输入依据、候选方案、风险解释、人工修改、采纳状态和执行结果。

## 7. Machine Physical Agent

### 7.1 定义

Machine Physical Agent 是软硬件一体的 cyber-physical agent。它不是给机床接一个数据网关，而是给加工设备安装感知器官、神经系统、边缘大脑、反射回路、记忆和 OEP 接口。

它的职责是：

- 理解当前 OEP。
- 采集机床、刀具、夹具、测量和安全状态。
- 参与 Gate 判断。
- 在人审后执行受控动作。
- 快速处理本地保护动作。
- 回写 ExecutionRecord、MeasurementResult、Exception 和事件。

### 7.2 六个组成部分

| 部分 | 内容 |
|---|---|
| Body | 机床本体、CNC、PLC、主轴、刀库、工作台、夹具、测头、对刀器 |
| Sensors | CNC/PLC、测头、激光对刀、主轴负载、电流、振动、AE、视觉、线激光、夹具/托盘、刀具身份、安全状态 |
| Nervous System | OPC UA、MTConnect、厂商 API、IO-Link、DAQ、工业以太网、相机触发、时间同步、边缘事件流 |
| Edge Brain | 机旁 IPC 或边缘 AI 盒，运行状态融合、Gate 判断、标准动作编排、解释与回写 |
| Reflex Loop | 急停、门锁、安全 PLC、CNC 报警、Feed Hold、刀具寿命不足、装夹未确认等本地快速阻断 |
| OEP Interface | 接收 OEP、检查 Gate、执行人审动作、回写 Trace |

实时安全由 CNC、PLC 和安全 PLC 保障。边缘 AI 负责状态理解、风险判断、解释和受控编排，不能替代安全 PLC。

### 7.3 三档能力规格

| 等级 | 名称 | 目标 | 行动边界 |
|---|---|---|---|
| L1 | MVP 感知版 | 让机床看得见、说得出 | 不自动执行，只参与 Gate 和追溯 |
| L2 | 受控执行版 | 让机床在批准后可行动 | 人审后执行，不自动启动主轴，不开放 Feed Override |
| L3 | 自适应增强版 | 让机床局部自适应 | 先建议，成熟后局部 Feed Override，仍受 OEP 和安全门约束 |

第一台验证机目标：

**L2 受控执行版 + L3 感知硬件预埋。**

### 7.4 第一台验证机感知器官

必选感官：

- CNC/PLC 数据接口。
- 工件测头。
- 激光对刀/断刀检测。
- 刀具、夹具、托盘身份确认。
- 边缘 HMI / 扫码终端。

增强感官也纳入第一台验证机硬件建设范围：

- 振动传感器。
- 工业相机 / 线激光。
- 主轴功率/电流高精度采集。
- 温度、冷却、气压传感。

增强感官在 V1 中的使用方式：

- 硬件部署和数据采集立即做。
- 用于证据采集、异常标签、离线分析、Agent 解释和下一单改进建议。
- 谨慎进入 Gate。
- 后续版本再逐步进入闭环控制。

### 7.5 第一台验证机受控执行动作

V1 可开放：

- 下发/绑定 NC 程序，但 CNC 启动仍由人操作。
- 触发测头找正、对刀、断刀检测等标准宏程序。
- 读取并回写 CNC 执行状态、报警、主轴负载、测量宏变量。
- 触发 Feed Hold / 报警停机等保护动作。
- Feed Override 暂不开放，自适应进给只做建议和离线分析。

每个命令必须关联：

- OEP。
- 审批记录。
- 操作者或触发 Agent。
- 执行结果。
- 异常记录。

## 8. 端到端首单流程

V1 第一条生产级首单闭环流程：

```text
订单/图纸进入
  -> DFM/报价
  -> 工艺/CAPP/CAM
  -> OEP 生成
  -> 仿真/审批
  -> 验证机受控执行
  -> 质量/异常回写
  -> 知识沉淀
```

### 8.1 订单/图纸进入

输入真实历史订单。系统创建 CustomerOrder、Part、Drawing、CADModel，并记录版本、附件、来源和责任人。

Agent 提取标题栏、材料、数量、关键尺寸和明显风险。工艺员补全缺失信息，补全内容形成结构化 diff。

### 8.2 DFM/报价

报价模块输出预算级报价、成本构成、风险假设和交期假设。正式报价承诺必须人审。

### 8.3 工艺/CAPP/CAM

Agent 生成工艺草案，工艺员补全或修正。系统记录依据、版本和采纳状态。CAM/NC 可由现有 CAM 工具或人工流程生成，但其结果必须成为对象并进入 OEP。

### 8.4 OEP 生成

Package / Gate Agent 生成工序/装夹级 OEP。父级订单包和零件批次包作为聚合视图。

### 8.5 仿真/审批

OEP 发布前通过 Engineering、Resource、Tool、Fixture、Simulation、Quality、Authority Gate。

### 8.6 验证机受控执行

Machine Physical Agent 根据 OEP 执行人审后的受控动作，采集必选和增强感官数据，回写执行状态。

### 8.7 质量/异常回写

执行结果写入 ExecutionRecord，测量结果写入 MeasurementResult，异常写入 Exception。

### 8.8 知识沉淀

每条 Agent 建议都要沉淀为 DecisionLog。被采纳或被修改的建议进入案例库和工艺模板改进候选。

## 9. 权限与安全

### 9.1 系统控制权

第一阶段系统必须具备：

- 记录权：完整记录订单、图纸、工艺、OEP、执行、质量。
- 建议权：生成 DFM/报价/CAPP/CAM/齐套建议。
- 放行权：未通过 OEP、仿真、审批、安全门，不进入受控试切流程。
- 受控执行权：人审后执行下发/绑定 NC、测量宏、对刀宏、Feed Hold 等动作。

记录权是 B/C/D 的地基，不能省略。

### 9.2 高风险动作策略

| 动作 | V1 策略 |
|---|---|
| 正式报价承诺 | 必须人审 |
| 工艺路线发布 | 必须工艺员确认 |
| NC 程序进入执行态 | 必须仿真/审批 |
| CNC 自动启动 | V1 不开放 |
| Feed Override | V1 不开放，只做建议和离线分析 |
| Feed Hold / 报警停机 | 可由 Machine Physical Agent 触发，但必须记录 |
| 替代材料 | 必须工程/质量审批 |
| 替代刀具超出规则 | 必须工艺审批 |
| 质量让步放行 | 必须质量负责人审批 |

## 10. 分阶段行动纲领

每个阶段必须同时推进三条轨道：OEP 操作内核、Agent 工作流、物理 Agent/产线硬件。

### 10.1 Phase 0：语义与样本冻结

周期：2-4 周。

目标：

- 选择真实历史订单和 A 类为主的零件样本。
- 冻结 OEP Plan/Gate/Trace schema。
- 冻结核心对象、事件 envelope、Agent 合同、工具注册表。
- 建立报价规则、工艺模板、资源主数据的最小知识库。
- 选定第一台验证机。
- 完成 Machine Physical Agent 的硬件 BOM、接口清单和安全边界。
- 跑通离线端到端：订单/图纸 -> 预算报价草案 -> 工艺草案 -> OEP 草案。

验收：

- 一份真实历史订单可生成预算报价草案、工艺草案和 OEP 草案。
- 人工补全和 Agent 建议都能进入 DecisionLog。

### 10.2 Phase 1：一台验证机首单闭环

周期：8-12 周。

目标：

- 四大内核达到产品级 MVP。
- 四个决策 Agent 跑通。
- Machine Physical Agent 达到 L2 受控执行版 + L3 感知硬件预埋。
- 必选感官和增强感官都安装并采集数据。
- OEP 通过仿真/审批后进入验证机受控执行。
- 执行、测量、异常、人工修改、Agent 建议采纳状态全部回写。

验收：

- Agent 在 DFM/报价、工艺路线、资源选择上有可采纳、可解释、可复盘价值。
- 高风险动作 100% Gate + 人审。
- OEP 能完整回放首单生产过程。

### 10.3 Phase 2：三台小单元复制

周期：12-20 周。

目标：

- 3 台设备接入统一 OEP 内核。
- 设备能力、刀具/夹具可用性、人员、检测资源进入资源选择和齐套判断。
- 引入局部排产、资源冲突检测、异常改派。
- Machine Physical Agent 标准化复制，形成可部署模板。
- 质量和执行数据开始反哺报价、工艺模板和资源选择。

验收：

- 多个 OEP 能跨 3 台设备形成可追溯、可调度、可冲突处理的小单元闭环。

### 10.4 Phase 3：20 台产线建设

目标：

- 扩展到约 20 台加工设备。
- 标准化 Machine Physical Agent 部署。
- 建设边缘设备、刀具/夹具/检测/物流协同。
- 引入更完整 Robot/Logistics Agent、Toolroom Agent、Inspection Agent。
- 强化运维、治理、复制和异常管理。

重点：

- 不重新设计架构。
- 复制并标准化 Phase 1/2 已验证的 OEP 内核、Agent 工作流和 Machine Physical Agent。

## 11. 验收指标

V1 最重要的验收不是单纯交付一件产品，而是证明 Agent 建议可以被工业流程采纳、解释、审计、复盘并改进下一单。

### 11.1 第一优先：智能闭环

候选指标：

- DFM/报价建议采纳率。
- 工艺路线建议采纳率。
- 刀具/夹具/机床选择建议采纳率。
- 人工修改差异可追踪率。
- Agent 建议依据完整率。
- 建议执行结果回写率。
- 可复用规则或模板更新数量。

### 11.2 地基：工程闭环

- 图纸到 OEP 数据链完整率。
- 关键对象版本一致率。
- OEP Plan/Gate/Trace 完整率。
- 人工补全结构化记录率。

### 11.3 地基：安全闭环

- 高风险动作 Gate 覆盖率 100%。
- 人审记录覆盖率 100%。
- 例外绕行记录率 100%。
- 物理 Agent 命令可追溯率 100%。

### 11.4 生产闭环

- 验证机按 OEP 完成首单执行。
- ExecutionRecord、MeasurementResult、Exception 可回放。
- OEP 与现场实际刀具、夹具、NC、测量结果一致。

## 12. 关键风险与应对

| 风险 | 说明 | 应对 |
|---|---|---|
| 范围过大 | 20 台产线、Agent、硬件、自适应控制同时推进 | 用 Phase 0/1/2/3 降低风险，第一实践阶段只打穿 1 台验证机 |
| Agent-first 失控 | Agent 成为事实主轴，后续难治理 | OEP 是事实主轴，Agent 输出必须进入对象、OEP、DecisionLog、事件 |
| 物理 Agent 退化成网关 | 只采集数据，不形成机床智能体 | 定义感知器官、边缘大脑、反射回路、OEP 接口和三档能力规格 |
| 数据质量不足 | 早期缺少历史数据和结构化工艺知识 | V1 以专家规则和工艺模板为主，同时记录建议、修改和执行结果 |
| 报价责任风险 | AI 报价直接承诺价格和交期 | V1 做预算级，正式承诺必须人审 |
| 自适应控制风险 | 过早开放 Feed Override | 第一台验证机只做建议和离线分析，不开放闭环控制 |
| 现场接受度低 | 工艺员不信任黑箱 | 作业卡双形态、人工修改 diff、建议依据和采纳状态可见 |
| 安全边界不清 | AI 与安全 PLC/CNC 权限混淆 | 实时安全归 CNC/PLC/安全 PLC，AI 做状态理解和受控编排 |

## 13. 最终建议

V1 的关键不是“一次性建成 20 台设备全自治工厂”，而是先让一台验证机在真实历史订单上跑通生产级首单闭环，并证明三件事：

1. OEP 能成为可靠的工业执行契约。
2. Agent 能在 DFM/报价、工艺路线、资源选择上产生可采纳、可解释、可复盘的建议。
3. Machine Physical Agent 能让机床拥有感知、边缘判断、受控动作和可追溯回写能力。

当这三件事跑通，20 台产线扩展就不是重新发明系统，而是复制、标准化、治理和持续增强。
