# 使用教程



1. 安装
    ```# 推荐拉最新的仓库
    git clone https://github.com/open-compass/VLMEvalKit.git
    
    cd VLMEvalKit
    pip install -e .

    # for qwen, check qwen仓库是否有依赖
    ```

2. 配置环境变量
    ```
    cd VLMEvalKit
    vim .env

    OPENAI_API_KEY=sk-sdaXMaExvyHiPGFhalQU4wgj1biTlRI8BgIzgp0cdUaDGG55
    OPENAI_API_BASE=http://35.220.164.252:3888/v1/chat/completions
    ```

3. 修改模型，如果非官方结构，https://github.com/open-compass/VLMEvalKit/blob/main/docs/zh-CN/Development.md
    ```
    cd VLMEvalKit

    vim vlmeval/config.py(project/benchmark/eval_vlmevalkit/VLMEvalKit/vlmeval)

    在这里修改路径： # eval_qwen.sh, 通过替换文本自动更换路径
        "Qwen2.5-VL-3B-Instruct": partial(
            Qwen2VLChat,
            model_path="Qwen/Qwen2.5-VL-3B-Instruct", # xxxxlocal path
            min_pixels=1280 * 28 * 28,
            max_pixels=16384 * 28 * 28,
            use_custom_prompt=False,
        )

    ```

4. 评测

    评测：MMBench_TEST_EN_V11 POPE TextVQA_VAL
    ``` bash
    export LMUData=/path/to/your/data # 数据缓存地址
    OUTPUT_DIR = "" # 评测结果

    # 评测MMBench_TEST_EN_V11 POPE TextVQA_VAL
    torchrun --nproc-per-node=2 run.py --data MMBench_TEST_EN_V11 POPE TextVQA_VAL --model Qwen2.5-VL-3B-Instruct --work-dir ${OUTPUT_DIR} --verbose 

    # 如果需要使用历史结果（前一天），加上--reuse
    ```
    评测CC-OCR，参考: VLMEvalKit/vlmeval/dataset/utils/ccocr_evaluator/README.md，额外安装：
    ```
    apted
    filetype
    httpx
    lxml
    nltk
    retry
    rich
    tabulate
    tiktoken
    tqdm
    zss
    dashscope
    ```