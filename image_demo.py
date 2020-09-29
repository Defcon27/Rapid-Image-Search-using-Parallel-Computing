import os
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotRGBDistribution(image, axis):

    df = pd.DataFrame()
    df["Intensity"] = image[:, :, 0].ravel()
    df["color"] = "b"
    df2 = pd.DataFrame()
    df2["Intensity"] = image[:, :, 1].ravel()
    df2["color"] = "g"
    df3 = pd.DataFrame()
    df3["Intensity"] = image[:, :, 2].ravel()
    df3["color"] = "r"
    df = df.append(df2)
    df = df.append(df3)

    sns.histplot(df, x="Intensity", bins=256, hue="color",
                 element="step", palette=["C0", "C2", "tomato"], ax=axis)


def plotGrayDistribution(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.hist(image.ravel(), bins=255, color="gray")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")
