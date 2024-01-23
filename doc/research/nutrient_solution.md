<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2024-01-23 16:47:25
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-01-23 18:29:08
 * @FilePath: /smart_hydroponic_farm/doc/research/nutrient_solution.MD
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 水耕營養液的組成與調配

## 文獻資料

無土栽培系統中水培養液的組成和準備對於植物的成功栽培至關重要。研究為此主題提供了寶貴的見解：

1. **養液組成**：水培養液通常包括植物生長所需的大量元素和微量元素的平衡。沒有一種通用的解決方案，具體組成取決於作物、環境條件和使用的系統。在準備這些解決方案時，平衡陽離子和陰離子是一個重點（Sathyanarayan、Warke、Mahajan 和 Annapure，2022）。 <cite>[Sathyanarayan, Warke, Mahajan, & Annapure, 2022][1]</cite>

[1]: https://consensus.app/papers/soil-availability-plants-sathyanarayan/0846420fff065cc1b22008628f6d9f11/

2. **化學可行性**：必須考慮水培養液的化學可行性區域。這涉及確保離子濃度不會沉澱，從而維持所需的養分組成（Rijck 和 Schrevens，1999）。 <cite>[Rijck & Schrevens, 1999][2]</cite>

[2]: https://consensus.app/papers/chemical-feasibility-region-solutions-plant-nutrition-rijck/5f44fb3d0d5655249b7f4c35027a2f0e/

3. **有機肥料**：有機肥料可以為水培系統提供溶解形式的必需營養素。可以從有機糞肥提取物中配製養液，這可以有助於可持續的食品生產（Ortiz，2020）。 <cite>[Ortiz, 2020][3]</cite>

[3]: https://consensus.app/papers/solutions-formulated-organic-fertilizers-ortiz/ee227f83714953138f152b8b26097772/

4. **自動化組成控制**：可在封閉的水培系統中使用自動化來補充和重複使用養液。這涉及調整營養素和水的濃度，以維持目標電導率（Savvas 和 Manos，1999）。 <cite>[Savvas & Manos, 1999][4]</cite>

[4]: https://consensus.app/papers/automated-composition-control-nutrient-solution-closed-savvas/e29c0ca2f936561595df19f26abb5694/

5. **養分濃度與植物生長**：溶液中的養分濃度影響植物的生長特性、葉綠素含量和養分吸收。不同的施肥制度對植物健康和產量有不同的影響（Nkcukankcuka、Jimoh、Griesel 和 Laubscher，2021）。 <cite>[Nkcukankcuka, Jimoh, Griesel, & Laubscher, 2021][5]</cite>

[5]: https://consensus.app/papers/growth-characteristics-chlorophyll-nutrients-nkcukankcuka/28a8d4f1e45156c897c444a0d68b787d/

6. **自動感測和控制**：計算機控制的系統配備離子選擇性電極，可以管理水培溶液中的大量營養素。這項技術允許直接測量和控制特定營養素濃度（Jung、Kim、Kim、Kang 和 Choi，2013）。 <cite>[Jung, Kim, Kim, Kang, & Choi, 2013][6]</cite>

[6]: https://consensus.app/papers/automated-sensing-control-hydroponic-macronutrients-jung/d4b012e274ee5cb59dbc089255f329c4/

7. **植物毒性化合物的積累**：在重複使用的養液中，可能會積累對植物生長有影響的植物毒性有機酸。減輕這些影響的方法包括向溶液中添加活性炭（Lee、Lee 和 Lee，2006）。 <cite>[Lee, Lee, & Lee, 2006][7]</cite>

[7]: https://consensus.app/papers/accumulation-phytotoxic-acids-reused-solution-lee/49667dd6ae8357afaa345f8df78b6855/

8. **養液動態模擬**：動態模型可以根據氣候變量預測養液的組成，有助於分析和控制水培系統（Giaglaras、Lykas 和 Kittas，1998）。 <cite>[Giaglaras, Lykas, & Kittas, 1998][8]</cite>

[8]: https://consensus.app/papers/dynamic-simulation-nutrient-solution-composition-closed-giaglaras/7df6c521ad31562884fa51366ae0b9f2/

這些研究強調了精心設計水培養液的重要性，考慮到諸如營養平衡、化學相互作用以及使用技術進行精確控制和優化等因素。

## 總結

根據文獻資料，以下是我們決定的方法：

### 營養液組成

主要成份由 N、K、Ca，比例為 1:0.6:0.8，並且添加微量元素。

其中微量元素包含：

- Fe
- Mn
- Zn
- Cu
- P

與有助於植物生長之細菌。

### 澆灌設施注意問題

在論文中有提到許多水循環的問題，像是：

- 植物毒性化合物的積累
- 每個植物的養分吸收速率不同
- 化學元素的性質不同

這幾點需要特別注意，並且在設計水循環系統時，需要考慮到這些問題。

## 參考資料

- [Sathyanarayan, Warke, Mahajan, & Annapure, 2022][1]
- [Rijck & Schrevens, 1999][2]
- [Ortiz, 2020][3]
- [Savvas & Manos, 1999][4]
- [Nkcukankcuka, Jimoh, Griesel, & Laubscher, 2021][5]
- [Jung, Kim, Kim, Kang, & Choi, 2013][6]
- [Lee, Lee, & Lee, 2006][7]
- [Giaglaras, Lykas, & Kittas, 1998][8]
