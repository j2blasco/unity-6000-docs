* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor-isFallback.html

#  [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html).isFallback
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
isFallback; 
### Description
If true, match this editor only if all non-fallback editors do not match. Defaults to false.
Unity does a two-pass match to hook up editors with inspected types. First the non-fallback editors are tested, and if none match, then the fallbacks are tested for a match. Setting this flag lets you set up a default editor for a given type, while still permitting another editor type to override it.
* * *
