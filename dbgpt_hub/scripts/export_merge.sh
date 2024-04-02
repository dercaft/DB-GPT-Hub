# llama2 series
python dbgpt_hub/train/export_model.py \
    --model_name_or_path defog/sqlcoder-7b-2 \
    --template llama2 \
    --finetuning_type lora \
    --checkpoint_dir dbgpt_hub/output/adapter/sqlcoder-sql-lora \
    --output_dir dbgpt_hub/output/sqlcoder-sql-sft \
    --fp16
# --model_name_or_path defog/sqlcoder-7b-2 /mnt/store/llama2-checkpoints-plus-sft-v3/checkpoint-14000/
# --checkpoint_dir dbgpt_hub/output/adapter/sqlcoder-sql-lora        dbgpt_hub/output/adapter/Siyuan-sql-lora
# --output_dir dbgpt_hub/output/sqlcoder-sql-sft        dbgpt_hub/output/Siyuan-sql-sft


## Baichuan2
# python dbgpt_hub/train/export_model.py \
#     --model_name_or_path Your_base_model_path_like_Baichuan2-13B-Chat \
#     --template Your_template_like_baichuan2_eval \
#     --finetuning_type lora \
#     --checkpoint_dir Your_ckpt_path_checkpoint-100 \
#     --output_dir Your_export_model_like_output_merge_model_baichuan2-13b-qlora_merge \
#     --fp16
#     # --bf16