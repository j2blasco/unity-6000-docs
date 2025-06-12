* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-debug-views.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Upscaling resolution in URP with Spatial-Temporal Post-Processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/change-resolution-scale-urp.html)
  * Spatial-Temporal Post-processing Rendering Debugger reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-enable.html)
Enable Spatial-Temporal Post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universal-additional-camera-data.html)
Access camera data with the Universal Additional Camera Data component in URP
# Spatial-Temporal Post-processing Rendering Debugger reference for URP
There are six debug views for Spatial-Temporal Post-processing (STP). To access them, open the Rendering Debugger window and navigate to **Rendering** > **Map Overlays** and select **STP**. Unity shows the **STP Debug Views** property where you can select one of the views.
For more information on how to access the Rendering Debugger window, refer to [How to access the Rendering Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html).
## Debug views
**Debug view** | **Description**  
---|---  
**Clipped Input Color** | Show the **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) input color clipped between 0 and 1.  
**Log Input Depth** | Show the input depth in logarithmic scale.  
**Reversible Tonemapped Input Color** | Show the input color mapped to a 0–1 range with a reversible tonemapper.  
**Shaped Absolute Input Motion** | Visualize the input motion vectors.  
**Motion Reprojection** | Visualize the reprojected color difference across several frames.  
**Sensitivity** | Visualize the pixel sensitivities. Green areas show where STP can’t predict motion behavior. These areas are likely to render with reduced visual quality. STP struggles to predict motion in areas when occluded objects first become visible or when there is fast movement. Incorrect object motion vectors can also cause issues with motion prediction.  
  
Red areas highlight pixels that are excluded from TAA, so STP intentionally does not predict their motion. This helps avoid unnecessary blurring and ghosting, especially when rendering transparent objects.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-enable.html)
Enable Spatial-Temporal Post-processing in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universal-additional-camera-data.html)
Access camera data with the Universal Additional Camera Data component in URP
