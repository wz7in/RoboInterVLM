export LMUData=/mnt/inspurfs/efm_t/sys2_data/LMU_for_VLMEVALKIT/

echo LMUData: $LMUData

MODEL_NAME="Qwen2.5-VL-3B-Instruct"

VLMEVALKIT_PATH="/mnt/petrelfs/wangziqin/project/System2VLA/eval/benchmark/eval_vlmevalkit/VLMEvalKit"
CONFIG_PATH="${VLMEVALKIT_PATH}/vlmeval/config.py"

# 要循环的模型路径列表， qwen25必须在model path路径中
MODEL_PATH_LIST=(
    "/mnt/petrelfs/wangziqin/project/System2VLA/playground/Pretrained_models/RoboBrain2.0-3B"
)

# qwen_json相关json拷贝到微调后的模型，可以实现将原版json
# qwen_json=/mnt/petrelfs/share/efm_p/zhuyangkun/share_model/qwen_25_vl_json

# 进入工作目录
cd "$VLMEVALKIT_PATH" || exit 1

# 循环处理每个模型路径
for MODEL_PATH in "${MODEL_PATH_LIST[@]}"; do
  echo "🔧 当前模型路径：$MODEL_PATH"

  # echo "  补全json：$MODEL_PATH"
  # cp $qwen_json/* $MODEL_PATH

  OUTPUT_DIR="$MODEL_PATH/eval_rlt/vlmevalkit"
  mkdir -p "$OUTPUT_DIR"
  
  # 修改 config.py 中第1255行
  echo "🔁 修改 config.py 中第1255行的 model_path"
  sed -i "1326s|model_path=\"[^\"]*\"|model_path=\"$MODEL_PATH\"|" "$CONFIG_PATH"

  # 可选：显示验证
  sed -n '1326p' "$CONFIG_PATH"

  # 执行评测
  echo "🚀 开始评测模型：$MODEL_PATH"
  # torchrun --nproc-per-node=8 run.py --data MMVet COCO_VAL POPE TextVQA_VAL OCRBench COCO_VAL \
  #   --model "$MODEL_NAME" \
  #   --work-dir "$OUTPUT_DIR" \
  #   --verbose \
  #   --reuse

  torchrun --nproc-per-node=8 run.py --data MMVet  \
    --model "$MODEL_NAME" \
    --work-dir "$OUTPUT_DIR" \
    --verbose \
    --reuse

  echo "✅ 评测完成：$MODEL_PATH"
  echo "-----------------------------------------"
done
