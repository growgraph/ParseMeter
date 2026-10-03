Step3. Divide the region into 10“ equal small regions.

Step4. Label the small regions by 1, 2...... m according to the inside samples’ class.

Step5. Remerge the frontiers of the same class regions in where is the same class then save it as a link table.

Step6. For any regions where there are training samples from different classes in the same unit, go to Step2.

Step7. Repeat the above until there is no region where there are different classes.

At the end, some separating hyper surfaces, which are described by the link tables, are obtained.

After learning from the training sample, the explorationist’s classification experience is collected in the hyper surface, i.e. link table. Using hyper surface the absent data can be estimated or predicted from data such as well logging. The steps are as following.

Step1. Input a testing sample and make a radial from the sample. Step2. Input all link tables of class k (k= 1,2,3......,m) obtained by the above training algorithm.

Step3. Count the intersecting number of the sample with the above link table.

Step4. If the intersecting number of the sample with the above link tables is odd then label the sample by & . It is mean that the prediction value is the th decision value, otherwise go to next step.

Step5. Input all link tables of class +1 obtained by the above training algorithm. Do step3-4 untilk =m.

Step6. Calculate the classifying accuracy rate.

This is a universal prediction method for large nonlinear data bases. In fact, For large data sets (10’) (see Table 1 and Table 2) , the speed of HSC is very fast. The reason is that the time of saving and extracting hyper surfaces is very short and the need for storage is very little, which is not the advantage of SVM. Another reason is that the decision process is very easy by using the Jordan Curve Theorem.

<table><thead><tr><th>italtlils Training Samples</th><th>Training Time</th><th>Recall Time</th><th>The Rate of Recall (%)</th></tr></thead><tbody><tr><td>3,314</td><td>Is</td><td>2s</td><td>100.00</td></tr><tr><td>6,677</td><td>3s</td><td>4s</td><td>100.00</td></tr><tr><td>9,525</td><td>4s</td><td>7s</td><td>100.00</td></tr><tr><td>9,530</td><td>6s</td><td>7s</td><td>100.00</td></tr><tr><td>17,919</td><td>8s</td><td>12s</td><td>100.00</td></tr><tr><td>43,217</td><td>18s</td><td>31s</td><td>100.00</td></tr><tr><td>106,344</td><td>48s</td><td>Im 17s</td><td>100.00</td></tr><tr><td>1,053,125</td><td>9m Os</td><td>12m 29s</td><td>100.00</td></tr></tbody></table>
