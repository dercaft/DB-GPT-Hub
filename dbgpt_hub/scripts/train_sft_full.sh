wandb offline # Close wandb
# a100 ,单卡
current_date=$(date +"%Y%m%d_%H%M")
train_log="dbgpt_hub/output/logs/train_sft_test_${current_date}.log"
start_time=$(date +%s)
echo " Train Start time: $(date -d @$start_time +'%Y-%m-%d %H:%M:%S')" >>${train_log}

# default train , zero-shot, 
num_shot=0

# one-shot train
# num_shot=1

dataset="example_text2sql_train"
if [ "$num_shot" -eq 1 ]; then
    dataset="example_text2sql_train_one_shot"
fi
model_name_or_path="/mnt/store/llama2-checkpoints-plus-sft-v3/checkpoint-14000/"   
output_dir="dbgpt_hub/output/adapter/Siyuan-sql-full"


# 多卡，deepseed，全量微调
deepspeed --include localhost:0,1,2,3 --master_port=29505 dbgpt_hub/train/sft_train.py \
    --dataset $dataset \
    --model_name_or_path $model_name_or_path \
    --do_train \
    --finetuning_type full \
    --max_source_length 2048 \
    --max_target_length 512 \
    --template llama2 \
    --output_dir $output_dir \
    --overwrite_cache \
    --overwrite_output_dir \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 16 \
    --lr_scheduler_type cosine_with_restarts \
    --logging_steps 50 \
    --learning_rate 1e-5 \
    --num_train_epochs 4 \
    --plot_loss \
    --bf16 True\
    --deepspeed dbgpt_hub/configs/ds_config.json 2>&1 | tee ${train_log}
    
echo "############train end###############" >>${train_log}
echo "Train End time: $(date)" >>${train_log}
end_time=$(date +%s)
duration=$((end_time - start_time))
hours=$((duration / 3600))
min=$(( (duration % 3600) / 60))
echo "Time elapsed: ${hour}  hour $min min " >>${train_log}
