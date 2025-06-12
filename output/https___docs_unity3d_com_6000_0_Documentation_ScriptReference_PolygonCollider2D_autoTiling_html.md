* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D-autoTiling.html

#  [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html).autoTiling
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
autoTiling; 
### Description
Determines whether the PolygonCollider2D's shape is automatically updated based on a SpriteRenderer's tiling properties.
When this is true, the Collider's shape is generated from a SpriteRenderer, if one exists as a component of the parent GameObject. The shape generated is dependent on the [SpriteRenderer.drawMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-drawMode.html). Regeneration happens when the `autoTiling` property is set to true, and subsequently every time a change is detected in the associated SpriteRenderer.
* * *
