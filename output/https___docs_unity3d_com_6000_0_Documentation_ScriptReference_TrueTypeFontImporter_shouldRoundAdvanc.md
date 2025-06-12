* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-shouldRoundAdvanceValue.html

#  [TrueTypeFontImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.html).shouldRoundAdvanceValue
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
shouldRoundAdvanceValue; 
### Description
Set this property to true if you want to round the internal advance width of the font to the nearest integer.
When positioning characters, the cumulated error induced by a rounded advance width may cause the spacing between characters to look inconsistent. Note that the integer [CharacterInfo.advance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterInfo-advance.html) is always rounded to the nearest integer, independently of this flag.
* * *
