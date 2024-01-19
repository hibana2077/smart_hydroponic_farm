<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2024-01-13 10:56:28
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2024-01-19 09:17:13
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

#### 光質控制

根據[《Plant Height Control by Photoselective Filters: Current Status and Future Prospects》](https://doi.org/10.21273/HORTTECH.9.4.618)一文的研究，通過調節紅光與遠紅光的比例，我們可以有效地控制作物的生長高度。例如，白熾燈的紅光(波長：660 nm)與遠紅光(波長：730 nm)比例較低，這促使植物的莖部延長；而螢光燈的比例較高，則有助於使植物保持矮小和緊湊的生長形態。

基於這些發現，當設計用於控制植物生長的照明系統時，選擇能夠提供調節光譜功能的LED燈尤為重要。這樣的LED燈不僅能夠提供適宜的光環境，更能夠根據作物的具體需求，精確調整光線的質量和強度，從而達到最佳的促進生長效果。

| 燈光類型 | 紅光/遠紅光比例 | 影響 |
| --------- | --------------- | ---- |
| 白熾燈 | 低 | 促使植物莖部延長 |
| 螢光燈 | 高 | 促使植物矮化和緊湊 |

#### 水分控制

根據[《Controlled Water Deficit as an Alternative to Plant Growth Retardants for Regulation of Poinsettia Stem Elongation》](https://doi.org/10.21273/HORTSCI.50.4.565)一文的研究，研究目的是比較使用植物生長抑制劑（PGRs）和控制水分赤字（WD）來控制一品紅‘Classic Red’的高度。研究發現，使用水分赤字的方法能夠有效地控制植物的高度，而且與使用PGRs相比，對植物品質（如葉片大小和顏色）的影響較小。實驗結果顯示，控制水分赤字是一種環保且成本較低的方法，可以作為控制一品紅高度的替代或輔助手段。

不過該篇論文並未討論水分赤字的具體可以壓低多少高度，因此我們需要進一步的研究。

#### 水中鹽分控制

根據[《Assessing the Effects of Irrigation Water Salinity on Two Ornamental Crops by Remote Spectral Imaging》](https://doi.org/10.3390/agronomy11020375)一文的研究，研究目的是探討鹽分對植物高度的影響。研究發現，鹽分可以有效地抑制植物的生長，並且鹽分越高，抑制效果越明顯。實驗結果顯示，當灌溉水的鹽度達到一定水平時，兩種觀賞植物的生長會受到影響。具體來說，對於洋紫荊，當灌溉水鹽度達到7.0 dS/m時，其生長顯著受到抑制；對於曼德維拉，當灌溉水鹽度達到4.0 dS/m時，生長受到顯著抑制。該研究提供了重要的數據，有助於了解灌溉水鹽度對觀賞植物生長的具體影響，對於改進灌溉策略和保護觀賞植物具有重要意義。

## 結論

根據上面所查閱的文獻，我們可以得出以下結論：

確實有辦法透過環境去影響作物的生長高度，但是這些方法都有各自的缺點，例如光質控制需要特殊的燈具，水分控制需要特殊的灌溉系統，水中鹽分控制需要特殊的灌溉水源。而且每個都需要再次實驗，才能得出有效的控制高度的方法。

所以會先採用水分控制：這個方法比較簡單，但是需要再次實驗，才能得出有效的控制高度的方法。

## 參考文獻

1. [Plant Height Control by Photoselective Filters: Current Status and Future Prospects](https://doi.org/10.21273/HORTTECH.9.4.618)
2. [Controlled Water Deficit as an Alternative to Plant Growth Retardants for Regulation of Poinsettia Stem Elongation](https://doi.org/10.21273/HORTSCI.50.4.565)
3. [Assessing the Effects of Irrigation Water Salinity on Two Ornamental Crops by Remote Spectral Imaging](https://doi.org/10.3390/agronomy11020375)