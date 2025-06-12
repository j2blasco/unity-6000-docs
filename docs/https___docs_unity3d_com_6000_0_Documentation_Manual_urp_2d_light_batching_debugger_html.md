* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-batching-debugger.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * [Optimizing 2D lights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-optimize.html)
  * Check how Unity batches lights


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-batching-intro.html)
Introduction to 2D light batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html)
2D Renderer asset component reference for URP
# Check how Unity batches lights
To open and use the debugger, follow these steps:
  1. Open the debugger window by going to **Window > 2D > Light Batching Debugger**.  
![Opening the Light Batching Debugger window](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/light-batching-debugger-0.png)
  2. View the Light Batching Debugger updates in real time by keeping the Game view and the debugger window open at the same time.  
![Light Batching Debugger window without a selected batch.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/light-batching-debugger-1.png)
  3. Select a batch from the left side of the debugger window to view Lights and Shadow Casters in the current batch.  
![Light Batching Debugger window with selected batch.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/light-batching-debugger-2.png)  
Sorting Layers that are color coded differently means that they’re in different batches with different **Batch IDs** and aren’t batched together.  
![Differently color coded](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/light-batching-debugger-color-1.png)  
Sorting Layers that share the same color code are batched together and will share the same **Batch ID**.  
![Similarly color coded](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/light-batching-debugger-color-2.png)
  4. Select adjacent batches to compare the differences between the selected batches. The debugger window displays the Light(s) and Shadow Caster(s) included in each batch in separate panels.  
![Light Batching Debugger window](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/light-batching-debugger-3.png)  
In this example, **Light A** exists in **Batch 0** and not in **Batch 1**. The debugger provides instructions at the bottom of the window on what you need to do to have Unity batch the two selected batches together; that is, **Batch 0** contains **Light A** which currently only targets the **BG** Sorting Layer. By having **Light A** also target the **Default** Sorting Layer, Unity may be able to batch both **Batch 0** and **Batch 1** together.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-batching-intro.html)
Introduction to 2D light batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html)
2D Renderer asset component reference for URP
