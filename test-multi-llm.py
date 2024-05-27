
import autogen

gpt3_config = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
    filter_dict={
        "model": {
            "gpt-3.5-turbo"
        }
    }
)

gpt4_config = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
    filter_dict={
        "model": {
            "gpt-4-32k"
        }
    }
)

print(gpt4_config)