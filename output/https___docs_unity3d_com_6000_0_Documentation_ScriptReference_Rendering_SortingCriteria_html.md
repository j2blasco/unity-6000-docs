* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.html

# SortingCriteria
enumeration
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
How to sort objects during rendering.
Control the way Unity sorts objects before drawing them by using and combining these flags.  
  
The basic flags are: 
  * [SortingLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.SortingLayer.html),
  * [RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.RenderQueue.html),
  * [BackToFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.BackToFront.html),
  * [QuantizedFrontToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.QuantizedFrontToBack.html),
  * [OptimizeStateChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.OptimizeStateChanges.html),
  * [CanvasOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.CanvasOrder.html).


Multiple flags, when combined, are applied in the above order.  
  
Some commonly-used sorting combinations are provided for convenience. Use [CommonOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.CommonOpaque.html) for opaque objects. This combination of flags includes optimization for reducing draw state changes and draws roughly front-to-back to reduce drawing over the same pixels many times. Use [CommonTransparent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.CommonTransparent.html) for transparent objects, which need to be sorted from back to front before being drawn for them all to be visible.  
  
Additional resources: DrawingSettings.sorting, ScriptableRenderContext.DrawRenderers.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.None.html) | Do not sort objects.  
[SortingLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.SortingLayer.html) | Sort by renderer sorting layer.  
[RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.RenderQueue.html) | Sort by material render queue.  
[BackToFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.BackToFront.html) | Sort objects back to front.  
[QuantizedFrontToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.QuantizedFrontToBack.html) | Sort objects in rough front-to-back buckets.  
[OptimizeStateChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.OptimizeStateChanges.html) | Sort objects to reduce draw state changes.  
[CanvasOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.CanvasOrder.html) | Sort renderers taking canvas order into account.  
[RendererPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.RendererPriority.html) | Sorts objects by renderer priority.  
[CommonOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.CommonOpaque.html) | Typical sorting for opaque objects.  
[CommonTransparent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.CommonTransparent.html) | Typical sorting for transparencies.  
* * *
