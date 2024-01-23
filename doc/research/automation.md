<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2024-01-23 18:55:29
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-01-23 21:39:02
 * @FilePath: /smart_hydroponic_farm/doc/research/automation.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 自動化技術在水耕農業中的應用

## 文獻查閱

1. **Android應用集成的自動化水耕系統**: Nwulu, Suka, 和 Dogo (2021) 設計了一個具有物聯網和Android應用功能的自動化水淹排水水耕系統。這個系統整合了自動植物灌溉、水位和pH測量及控制系統，並利用Wi-Fi通訊技術實現遠程管理和控制 [(Nwulu et al., 2021)](https://consensus.app/papers/automated-hydroponic-system-integrated-with-android-nwulu/99174740ec5b5e2489bb8cb2c9e67672/)。

2. **物聯網基礎的智能水耕農業專家系統**: Raju et al. (2022) 提出了一個集成了移動應用和人工智能的智能水耕專家系統，該系統利用物聯網環境，並結合深度學習卷積神經網絡模型進行最佳營養水平預測和植物疾病檢測和分類 [(Raju et al., 2022)](https://consensus.app/papers/design-implementation-smart-hydroponics-farming-using-raju/3fcc5a6256a85cbb92f2b8953ff6308f/)。

3. **物聯網和機器學習算法驅動的自動化水耕系統**: Geethamani et al. (2022) 提出了一種使用機器學習算法預測農業參數的可靠自動化水耕系統。該系統使用卷積神經網絡和朴素貝葉斯算法進行感測器值預測和比較分析 [(Geethamani et al., 2022)](https://consensus.app/papers/design-development-reliable-automated-hydroponics-geethamani/425d5c47f58357908fcfbfab721e3bca/)。

4. **大數據支持的自動化水耕滴灌系統**: Ani 和 Gopalakirishnan (2020) 研究了利用大數據技術來跟踪和記錄營養物質值，從而進一步自動化水耕滴灌系統的可能性。這項工作強調了大數據在自動化水耕農業中的應用前景 [(Ani & Gopalakirishnan, 2020)](https://consensus.app/papers/automated-hydroponic-drip-irrigation-using-data-ani/fbc79ffd24115b60a028de7ede01e69a/)。

5. **垂直農業中的自動化技術**: Van Gerrewey, Boon, 和 Geelen (2021) 探討了在垂直農業系統中，自動化水耕栽培和先進的LED照明系統的技術進步。研究強調了自動化技術在提高水耕系統的循環性和彈性方面的潛力 [(Van Gerrewey et al., 2021)](https://consensus.app/papers/farming-only-gerrewey/d9640b2fea7e572095857f4190ee5298/)。

6. **基於NFT系統上的小型自動化採收機器人**: 這項研究提出了一種基於NFT系統上的小型自動化採收機器人，該機器人可以在水耕系統中自動採收蔬菜，同時也很小巧 [(Agrawal er ai.)](https://elibrary.asabe.org/abstract.asp?JID=5&AID=41742&CID=dall2012&T=1)。

綜合以上發現，可以看出自動化技術在水耕農業中的應用已經取得了重大進展，特別是在遠程管理、數據分析、營養控制和疾病檢測方面。這些技術的整合極大地提高了水耕農業的效率和產量，並為未來的發展提供了新的可能性。

## 統整

~~這裡還需要查閱上述論文的`Future Work`部分，並且統整出未來的發展方向。~~

### 已實現的自動化技術

- 植物疾病檢測和分類
- 植物營養控制
- 遠程管理
- 數據分析
- 機械手臂

### 我們能把現有的技術做到更好

- 數據分析
- 更完整的植物營養控制
- 通用植物疾病檢測和分類
- 小型化且可複用的機械手臂

### 我們能做到的創新點

- 基於多模態模型的植物疾病檢測和分類
- 基於大語言模型管理的全自動化水耕系統