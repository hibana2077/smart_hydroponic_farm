<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2024-01-13 10:56:28
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-01-13 18:11:20
 * @FilePath: /smart_hydroponic_farm/doc/research/crop_grow.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 作物生長和產量優化

## 問題

1. 透過環境控制，是否可以限制作物生長的高度？

## 方法

### 1, 透過環境控制，是否可以限制作物生長的高度？

可以，透過環境控制，可以限制作物生長的高度。

分為四種方法：

1. 光質控制
2. 水分控制
3. 水中鹽分控制
4. 養分控制

#### 光質控制

在設計用於植物生長的光照設備時，選擇合適的燈光類型和調整光譜成為關鍵因素。根據[《Plant Height Control by Photoselective Filters: Current Status and Future Prospects》](https://doi.org/10.21273/HORTTECH.9.4.618)一文的研究，通過調節紅光與遠紅光的比例，我們可以有效地控制作物的生長高度。例如，白熾燈的紅光(波長：660 nm)與遠紅光(波長：730 nm)比例較低，這促使植物的莖部延長；而螢光燈的比例較高，則有助於使植物保持矮小和緊湊的生長形態。

基於這些發現，當設計用於控制植物生長的照明系統時，選擇能夠提供調節光譜功能的LED燈尤為重要。這樣的LED燈不僅能夠提供適宜的光環境，更能夠根據作物的具體需求，精確調整光線的質量和強度，從而達到最佳的促進生長效果。

| 燈光類型 | 紅光/遠紅光比例 | 影響 |
| --------- | --------------- | ---- |
| 白熾燈 | 低 | 促使植物莖部延長 |
| 螢光燈 | 高 | 促使植物矮化和緊湊 |

#### 水分控制