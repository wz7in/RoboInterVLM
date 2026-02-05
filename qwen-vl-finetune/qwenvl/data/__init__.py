import re
import json
from pathlib import Path

##################################################################################
### REAL Dataset: Generation
##################################################################################

generation_root = "#TODO/Generation"

# rh20t 真机数据
rh20t_json_root = f"{generation_root}/meta/train/rh20t/smart_resize_format"
rh20t_image_root = f"{generation_root}/image/train/rh20t"

rh20t_vla_contact_box_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_contact_box_qa.json",
    "data_path": f"{rh20t_image_root}/contact_box",
}
rh20t_vla_contact_point_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_contact_point_qa.json",
    "data_path": f"{rh20t_image_root}/contact_point",
}
rh20t_vla_current_box_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_current_box_qa.json",
    "data_path": f"{rh20t_image_root}/current_box",
}
rh20t_vla_final_box_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_final_box_qa.json",
    "data_path": f"{rh20t_image_root}/final_box",
}
rh20t_vla_traj_init_point_qa_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_traj_qa.json",
    "data_path": f"{rh20t_image_root}/traj_init_point_qa",
}
rh20t_vla_traj_qa_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_traj_qa_wo_init_pos.json",
    "data_path": f"{rh20t_image_root}/traj_qa",
}
rh20t_vla_gripper_det_qa_train = {
    "annotation_path": f"{rh20t_json_root}/full_single_multi_contact_obj_gripper_det_qa.json",
    "data_path": f"{rh20t_image_root}/gripper_det_qa",
}

# droid 真机数据
droid_json_root = f"{generation_root}/meta/train/droid/smart_resize_format"
droid_image_root = f"{generation_root}/image/train/droid"

droid_vla_contact_box_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_contact_box_qa.json",
    "data_path": f"{droid_image_root}/contact_box",
}
droid_vla_contact_point_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_contact_point_qa.json",
    "data_path": f"{droid_image_root}/contact_point",
}
droid_vla_current_box_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_current_box_qa.json",
    "data_path": f"{droid_image_root}/current_box",
}
droid_vla_final_box_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_final_box_qa.json",
    "data_path": f"{droid_image_root}/final_box",
}
droid_vla_traj_init_point_qa_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_traj_qa.json",
    "data_path": f"{droid_image_root}/traj_init_point_qa",
}
droid_vla_traj_qa_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_traj_qa_wo_init_pos.json",
    "data_path": f"{droid_image_root}/traj_qa",
}
droid_vla_gripper_det_qa_train = {
    "annotation_path": f"{droid_json_root}/full_single_multi_contact_obj_gripper_det_qa.json",
    "data_path": f"{droid_image_root}/gripper_det_qa",
}


##################################################################################
### REAL Dataset: Understanding
##################################################################################

understanding_root = "#TODO/Understanding"

# rh20t choice 数据
rh20t_choice_json_root = f"{understanding_root}/meta/train/rh20t"
rh20t_choice_image_root = f"{understanding_root}/image/train/rh20t"

rh20t_contact_choice_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/contact_decide.json",
    "data_path": f"{rh20t_choice_image_root}/contact_decide",
}
rh20t_graspppose_choice_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/grasppose_choice.json",
    "data_path": f"{rh20t_choice_image_root}/grasppose_choice",
}
rh20t_grounding_choice_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/grounding_choice.json",
    "data_path": f"{rh20t_choice_image_root}/grounding_choice",
}
rh20t_traj_lang_choice_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/trajlang_choice.json",
    "data_path": f"{rh20t_choice_image_root}/trajlang_choice",
}
rh20t_traj_direction_choice_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/traj_direction_choice.json",
    "data_path": f"{rh20t_choice_image_root}/traj_direction_choice",
}
rh20t_traj_choice_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/traj_choice.json",
    "data_path": f"{rh20t_choice_image_root}/traj_choice",
}
rh20t_traj_direction_choice_with_traj_qa_train = {
    "annotation_path": f"{rh20t_choice_json_root}/traj_direction_choice_with_traj.json",
    "data_path": f"{rh20t_choice_image_root}/traj_direction_choice_with_traj",
}

# droid choice 数据
droid_choice_json_root = f"{understanding_root}/meta/train/droid"
droid_choice_image_root = f"{understanding_root}/image/train/droid"

droid_contact_choice_qa_train = {
    "annotation_path": f"{droid_choice_json_root}/contact_decide.json",
    "data_path": f"{droid_choice_image_root}/contact_decide",
}
droid_grounding_choice_qa_train = {
    "annotation_path": f"{droid_choice_json_root}/grounding_choice.json",
    "data_path": f"{droid_choice_image_root}/grounding_choice",
}
droid_traj_lang_choice_qa_train = {
    "annotation_path": f"{droid_choice_json_root}/trajlang_choice.json",
    "data_path": f"{droid_choice_image_root}/trajlang_choice",
}
droid_traj_direction_choice_qa_train = {
    "annotation_path": f"{droid_choice_json_root}/traj_direction_choice.json",
    "data_path": f"{droid_choice_image_root}/traj_direction_choice",
}
droid_traj_choice_qa_train = {
    "annotation_path": f"{droid_choice_json_root}/traj_choice.json",
    "data_path": f"{droid_choice_image_root}/traj_choice",
}
droid_traj_direction_choice_with_traj_qa_train = {
    "annotation_path": f"{droid_choice_json_root}/traj_direction_choice_with_traj.json",
    "data_path": f"{droid_choice_image_root}/traj_direction_choice_with_traj",
}

# manipvqa language data
manipvqa_json_root = f"{understanding_root}/meta/train/manipvqa"
manipvqa_image_root = f"{understanding_root}/image/train/manipvqa"
manipvqa_train = {
    "annotation_path": f"{manipvqa_json_root}/task_planning.json",
    "data_path": f"{manipvqa_image_root}/task_planning",
}


##################################################################################
# 将所有数据集注册到 data_dict
##################################################################################

data_dict = {
    "all": None,
    ############### REAL Dataset: Generation ###############
    # rh20t 真机数据
    "rh20t_vla_contact_box_train": rh20t_vla_contact_box_train,
    "rh20t_vla_contact_point_train": rh20t_vla_contact_point_train,
    "rh20t_vla_current_box_train": rh20t_vla_current_box_train,
    "rh20t_vla_final_box_train": rh20t_vla_final_box_train,
    "rh20t_vla_traj_qa_train": rh20t_vla_traj_qa_train,
    "rh20t_vla_traj_init_point_qa_train": rh20t_vla_traj_init_point_qa_train,
    "rh20t_vla_gripper_det_qa_train": rh20t_vla_gripper_det_qa_train,
    # droid 真机数据
    "droid_vla_contact_box_train": droid_vla_contact_box_train,
    "droid_vla_contact_point_train": droid_vla_contact_point_train,
    "droid_vla_current_box_train": droid_vla_current_box_train,
    "droid_vla_final_box_train": droid_vla_final_box_train,
    "droid_vla_traj_qa_train": droid_vla_traj_qa_train,
    "droid_vla_traj_init_point_qa_train": droid_vla_traj_init_point_qa_train,
    "droid_vla_gripper_det_qa_train": droid_vla_gripper_det_qa_train,
    ############### REAL Dataset: Understanding ###############
    # rh20t choice 数据
    "rh20t_contact_choice_qa_train": rh20t_contact_choice_qa_train,
    "rh20t_graspppose_choice_qa_train": rh20t_graspppose_choice_qa_train,
    "rh20t_grounding_choice_qa_train": rh20t_grounding_choice_qa_train,
    "rh20t_traj_lang_choice_qa_train": rh20t_traj_lang_choice_qa_train,
    "rh20t_traj_direction_choice_qa_train": rh20t_traj_direction_choice_qa_train,
    "rh20t_traj_choice_qa_train": rh20t_traj_choice_qa_train,
    "rh20t_traj_direction_choice_with_traj_qa_train": rh20t_traj_direction_choice_with_traj_qa_train,
    # droid choice 数据
    "droid_contact_choice_qa_train": droid_contact_choice_qa_train,
    "droid_grounding_choice_qa_train": droid_grounding_choice_qa_train,
    "droid_traj_lang_choice_qa_train": droid_traj_lang_choice_qa_train,
    "droid_traj_direction_choice_qa_train": droid_traj_direction_choice_qa_train,
    "droid_traj_choice_qa_train": droid_traj_choice_qa_train,
    "droid_traj_direction_choice_with_traj_qa_train": droid_traj_direction_choice_with_traj_qa_train,
    ############### REAL Dataset: Language ###############
    "manipvqa_train": manipvqa_train,
}


def parse_sampling_rate(dataset_name):
    match = re.search(r"%(\d+)$", dataset_name)
    if match:
        return int(match.group(1)) / 100.0
    return 1.0


def data_list(dataset_names):
    if dataset_names == ["all"]:
        dataset_names = list(data_dict.keys())
    config_list = []
    for dataset_name in dataset_names:
        sampling_rate = parse_sampling_rate(dataset_name)
        dataset_name = re.sub(r"%(\d+)$", "", dataset_name)
        if dataset_name in data_dict.keys():
            config = data_dict[dataset_name].copy()
            config["sampling_rate"] = sampling_rate
            config_list.append(config)
        else:
            raise ValueError(f"do not find {dataset_name}")
    return config_list


def count_data(data_dicts):
    for data_name in data_dicts:
        if data_dicts[data_name] is None:
            continue
        annotation_path = data_dicts[data_name]["annotation_path"]
        if annotation_path.endswith(".jsonl"):
            with open(annotation_path, "r") as f:
                data = f.readlines()
            print(data_name, len(data))
        else:
            with open(annotation_path, "r") as f:
                data = json.load(f)
            print(data_name, len(data))


if __name__ == "__main__":
    count_data(data_dict)
