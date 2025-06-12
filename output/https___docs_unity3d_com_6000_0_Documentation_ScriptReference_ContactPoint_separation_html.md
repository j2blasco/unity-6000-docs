* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint-separation.html

#  [ContactPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html).separation
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
separation; 
### Description
The distance between the colliders at the contact point.
This value represents how far apart or interpenetrated the two colliders are at the time the contact was registered: • A positive separation means the colliders are close but not touching, and the contact was generated in anticipation of a possible collision (due to contact offset thresholds). • A zero separation means the colliders are just touching, with their surfaces in contact but not overlapping. • A negative separation indicates that the colliders are overlapping — the more negative the value, the deeper the penetration at that point.  
  
This property is useful for examining how close colliders are, measuring contact depth in overlaps, or fine-tuning collision responses. During the lifetime of a collision, the separation may fluctuate due to simulation corrections, contact offset values, or changes in relative motion.
* * *
