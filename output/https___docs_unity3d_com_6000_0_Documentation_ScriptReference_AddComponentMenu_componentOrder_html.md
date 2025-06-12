* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu-componentOrder.html

#  [AddComponentMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html).componentOrder
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
componentOrder; 
### Description
The order of the component in the component menu (lower values appear higher in the menu).
**Note** : The order only affects the component item itself and doesn't influence any submenus.  
  
Scripts are first sorted by their namespace. Scripts without a namespace are positioned after those with a namespace.  
  
By default, menu items are assigned a position value of 20. The final placement of the item is determined by adding the `componentOrder` value to this default position. The order can be either positive or negative value.  
  
If your item has a priority of 11 or higher than the previous item, a separator is automatically added before your item in the menu.  
  
The following example uses a `componentOrder` of `-1` to bring **MyScript2** above **MyScript1** :
```
using UnityEngine;  
  

[AddComponentMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html)("My Scripts/My Script 1")]
public class MyScript1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}  
  
[AddComponentMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html)("My Scripts/My Script 2", -1)]
public class MyScript2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}

```

* * *
