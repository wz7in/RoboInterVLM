export LMUData=/mnt/petrelfs/share/efm_p/sys2_data/LMU_for_VLMEVALKIT/

echo LMUData: $LMUData

MODEL_NAME=(
  # "Qwen2.5-VL-3B-Instruct"
  # "Qwen2.5-VL-3B-Instruct"
  # "Qwen2.5-VL-3B-Instruct"
  # "Qwen2.5-VL-3B-Instruct"
  # "Qwen2.5-VL-3B-Instruct"
  # "Qwen2.5-VL-7B-Instruct"
  # "Qwen2.5-VL-3B-Instruct"
  # "Qwen2.5-VL-7B-Instruct"
  # "Qwen2.5-VL-32B-Instruct"
  # "InternVL3-1B"
  # "InternVL3-2B"
  # "InternVL3-8B"
  # "Phi-3.5-Vision"
  # "llava_onevision_qwen2_0.5b_ov"
  "llava_onevision_qwen2_7b_ov"
)

VLMEVALKIT_PATH="/mnt/petrelfs/wangziqin/project/System2VLA/eval/benchmark/eval_vlmevalkit/VLMEvalKit"
CONFIG_PATH="${VLMEVALKIT_PATH}/vlmeval/config.py"

# 要循环的模型路径列表， qwen25必须在model path路径中
MODEL_PATH_LIST=(
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/Qwen2.5-VL-3B-Instruct"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/Qwen2.5-VL-7B-Instruct"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/RoboBrain2.0-3B"
    # "/mnt/petrelfs/wangziqin/.cache/huggingface/hub/models--BAAI--RoboBrain2.0-7B/snapshots/d601a0b905d054c9f3b746c9ac3b18aec18110b0/"
    # "/mnt/petrelfs/wangziqin/.cache/huggingface/hub/models--BAAI--RoboBrain2.0-32B/snapshots/acf6af53caa98bf155f72e8235dfc0e3f0603b06/"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/InternVL3-1B"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/InternVL3-2B"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/InternVL3-8B"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_generaldata_wo_ao/checkpoint-14567"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_manipdata/checkpoint-18025"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_manipdata_coco/checkpoint-24904"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_manipdata_generaldata_wo_ao/checkpoint-32592"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_manipdata_llavaonevis/checkpoint-18865"
    # "/mnt/phwfile/efm_t/wangziqin/results/manip_sys2_qwen25_3b_gdata_udata_manipvqa_generaldata_droidcot"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_manipdata_cot/checkpoint-21242"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_cot/checkpoint-3218"
    # "/mnt/petrelfs/share/wangziqin/robotdata/results/manip_sys2_qwen25_3b_cot10e/checkpoint-32180"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/Phi-3.5-vision-instruct"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/qwen-vl-finetune/results/manip_sys2_qwen25_3b_gdata_udata_manipvqa_generaldata"
    # "/mnt/petrelfs/share/wangziqin/robotdata/playground/Pretrained_models/llava-onevision-qwen2-0.5b-ov"
    # "/mnt/petrelfs/wangziqin/project/System2VLA/qwen-vl-finetune/results/manip_sys2_qwen25_7b_gdata_udata_manipvqa_generaldata"
    "/mnt/petrelfs/wangziqin/project/System2VLA/qwen-vl-finetune/results/llava-one-vision-7B_gdata_udata_manipvqa_generaldata"
)

motified_lines=(
  # 1326
  # 1326
  # 1326
  # 1326
  # 1326
  # 1340
  # 1326
  # 1340
  # 1362
  # 972
  # 975
  # 979
  # 1212
  # 768
  771
)

# qwen_json相关json拷贝到微调后的模型，可以实现将原版json
# qwen_json=/mnt/petrelfs/share/efm_p/zhuyangkun/share_model/qwen_25_vl_json

# 进入工作目录
cd "$VLMEVALKIT_PATH" || exit 1

# 循环处理每个模型路径
for i in "${!MODEL_PATH_LIST[@]}"; do
  MODEL_PATH=${MODEL_PATH_LIST[$i]}
  echo "🔧 当前模型路径：$MODEL_PATH"

  # echo "  补全json：$MODEL_PATH"
  # cp $qwen_json/* $MODEL_PATH

  OUTPUT_DIR="$MODEL_PATH/eval_rlt/vlmevalkit"
  mkdir -p "$OUTPUT_DIR"
  
  # 修改 config.py 中第x行
  echo "🔁 修改 config.py 中第${motified_lines[$i]}行的 model_path"
  sed -i "${motified_lines[$i]}s|model_path=\"[^\"]*\"|model_path=\"$MODEL_PATH\"|" "$CONFIG_PATH"

  # 可选：显示验证
  sed -n "${motified_lines[$i]}p" "$CONFIG_PATH"

  # 执行评测
  echo "🚀 开始评测模型：$MODEL_PATH"
  # torchrun --nproc-per-node=8 run.py --data MMVet COCO_VAL TextVQA_VAL OCRBench POPE \
  #   --model "$MODEL_NAME" \
  #   --work-dir "$OUTPUT_DIR" \
  #   --verbose \
  #   --reuse

  torchrun --nproc-per-node=8 run.py --data MMVet \
    --model "${MODEL_NAME[$i]}" \
    --work-dir "$OUTPUT_DIR" \
    --verbose \
    --reuse

  echo "✅ 评测完成：$MODEL_PATH"
  echo "-----------------------------------------"
done
