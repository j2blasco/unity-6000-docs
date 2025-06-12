* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/introduction-to-rich-text-tags.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Work with text](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
  * [Style text with rich text tags](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)
  * Introduction to rich text tags


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)
Style text with rich text tags
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html)
Supported rich text tags
# Introduction to rich text tags
Rich text tags are tags that you can place inside a text string to style the text between the tags. 
**Note** : In the current release, rich text tags aren’t supported for [TextField](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/UIE-uxml-element-TextField.html).
## Rich text syntax
Rich text tags are similar to HTML or XML tags, but have less strict syntax.
A simple tag can have be just its name and have no additional values or attributes. For example, the `<b>` tag makes text bold.
Some tags have additional values or attributes like this:
  * `<tag="value">`
  * `<tag attribute="value">`


For example: 
  * `<color=”red”>`: Makes text red
  * `<sprite index=3>`: Inserts the fourth sprite from the default Sprite Asset.


**Note** : In a UXML file, you must use HTML code for the following characters:
  * `<`: `(&lt;)`
  * `>`: `(&gt;)`
  * `"`: `(&quot;)`


The following table lists possible attribute value types and example values.
**Value type** | **Example value**  
---|---  
Decimals | `0.5`  
Percentages | `25%`  
**Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) values | `5px`  
Font units | `1.5em`  
Hex color values |  `#FFFFFF` (RGB)  
`#FFFFFFFF` (RGBA)  
`#FF` (A)  
Names | Both `<link=”ID”>` and `<link=ID>` are valid.  
## Tag scope and nested tags
Tags have a scope that defines how much of the text they affect. Most tags affect all text from the point they appear onward.
For example, if you add the tag `<color="red">` to the beginning of the text, it affects the entire text block: `<color="red">This text is red`.
If you add the same tag in the middle of the text block, it affects only the text between the tag and the end of the block : `This text turns<color="red"> red`.
If you use the same tag more than once in a text block, the last tag supersedes all previous tags of the same type: `<color="red">This text goes from red<color="green"> to green`.
You can also use a closing tag to limit the scope of a tag, and use nested tag within another tag: `<color=red>This text is <color=green>mostly </color>red`.
The first `<color>` tag’s scope is the entire text block. The the second `<color>` tag has a closing tag that limits its scope to one word.
When you nest tags, you don’t need to close their scopes in the same order that you started them.
## Enable and disable rich text tags
Rich text tags are enabled by default. 
To disable the rich text tag, do one of the following:
  * In UI Builder, select the control and clear the **Enable Rich Text** checkbox in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
  * In UXML, set the `enable-rich-text` attribute to `false`.


## Additional resources
  * [Supported rich text tags](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html)
  * [Add hyperlinks in text](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/add-hyperlinks-in-text.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-rich-text-tags.html)
Style text with rich text tags
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-supported-tags.html)
Supported rich text tags
