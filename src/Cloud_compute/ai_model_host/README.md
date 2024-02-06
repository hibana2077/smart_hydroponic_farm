<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2024-02-06 13:32:07
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-02-06 16:28:49
 * @FilePath: /smart_hydroponic_farm/src/Cloud_compute/ai_model_host/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# AI model host api

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## 簡介

這個API是用來部署AI模型的，透過連上hugging face上的模型儲存空間，來動態部署模型。

## 開發者說明

請把模型上傳至[hibana2077/oasis](https://huggingface.co/hibana2077/oasis)的model資料夾，並且在`table.json`
中加入模型的資訊，格式如下：

```json
{
    //其他模型
    "oasis": {
        "path": "oasis.keras", // or "oasis.pt"
        "version": "1.0",
    }
}
```

目前只支援keras和pytorch的模型，位置起始於`hibana2077/oasis`的model資料夾。

如果有更新模型，請更新`table.json`的版本號，並且上傳新的模型，API會自動下載最新的模型。