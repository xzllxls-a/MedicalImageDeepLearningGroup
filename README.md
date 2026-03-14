# Medical Image Deep Learnig Group Code

## This repository contains code and sample data used by our research group.


关于医学图像（影像）的深度学习研究领域

一个研究工作的两个核心方面是：问题和方法。

对于医学图像（影像）处理领域的问题主要包含两个方面：图像形态和任务。

影像+任务+方法
（1）什么模态的影像：断层影像（Computed tomography, CT）？ 磁共振（Magnetic Resonance Imaging, MRI）？ 病理（Pathological image）？ 是用单模态，还是多模态？

（2）什么类型的任务：分类（Classification）？ 检测（Detection）？ 分割（Segmentation）？ 图像转换（Translation, Synthesis）？

（3）方法：什么模型？ 什么网络结构？ 是监督学习，无监督学习，还是半监督学习？ 处理流程是单阶段，还是双阶段甚至多阶段？

综述文章是对某个领域研究工作的梳理。阅读综述是了解一个研究领域的一个好办法。

Digital Imaging and Communications in Medicine — is the international standard for medical images and related information.
Medical image files are usually stored in the DICOM format.
DICOM file format reference:
https://www.dicomstandard.org


There are severial common image software to view, edit and process medical image data, including:
1. ImageJ:
https://imagej.net/ij/

2. Image2-Fiji:
https://imagej.net/software/fiji/

3. ITK-Snap:
https://www.itksnap.org/pmwiki/pmwiki.php


Pydicom is a pure Python package for working with DICOM files.

https://github.com/pydicom/pydicom

For using Pydicom in Python script, please import the package as following:
```python
import pydicom
```

Numpy is the fundamental package for data processing with Python.
For using Pydicom in Python script, please import the package as following:
```python
import numpy as np
```

## Commended Learning Resources
## 推荐的学习资源

### 一、 关于图像处理
1. 图书

冈萨雷斯, 伍兹 著. 阮秋琦 译. 数字图像处理. 电子工业出版社. 2017 （中文翻译版）

https://item.jd.com/12191950.html?spmTag=YTAyMTkuYjAwMjM1Ni5jMDAwMDQ2ODkuc2VhcmNoX2NvbmZpcm0lMkNhMDI0MC5iMDAyNDkzLmMwMDAwNDAyNy4xJTIzc2t1X2NhcmQ&pcdk=u7iH-J4K4CjUyILE5VJ1a2mb5kg_Oe33e_ZY6DEpbTQ%3D.rQ4a.tlbT


### 二、 关于机器学习或深度学习

1. 图书

(1) 周志华. 机器学习. 清华大学出版社

(2) Ian Goodfellow, Yoshua Bengio, Aaron Courville. Deep learning. MIT Press, 2016

https://www.deeplearningbook.org/

中文翻译版：

Ian Goodfellow著，赵申剑，黎彧君，符天凡、李凯译. 深度学习. 人民邮电出版社, 2017

纸质书：

https://item.jd.com/12128543.html?spmTag=YTAyMTkuYjAwMjM1Ni5jMDAwMDQ2ODkuc2VhcmNoX2NvbmZpcm0lMkNhMDI0MC5iMDAyNDkzLmMwMDAwNDAyNy4xJTIzc2t1X2NhcmQ

电子版：

https://github.com/exacity/deeplearningbook-chinese
 

2 教学视频

(1) 周志华老师亲讲-西瓜书全网最详尽讲解-1080p高清原版《机器学习初步》

https://www.bilibili.com/video/BV1gG411f7zX/?spm_id_from=333.337.search-card.all.click

(2) （2025版）李宏毅机器学习深度学习系列课程全集，公认体验感最好的入门课程！--人工智能/机器学习/深度学习

https://www.bilibili.com/video/BV1TAtwzTE1S/?spm_id_from=333.337.search-card.all.click&vd_source=73e26f76b70b859ab03ff8feced6d099