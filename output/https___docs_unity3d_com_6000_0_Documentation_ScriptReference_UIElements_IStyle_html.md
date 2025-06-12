* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle.html

# IStyle
interface in UnityEngine.UIElements
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
This interface provides access to a VisualElement inline style data. 
Reading properties from this object will read from the inline style data for this element. To read the style data computed for the element use [IStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle.html) interface. Writing to a property will mask the value coming from USS with the provided value however other properties will still match the values from USS. 
### Properties
Property | Description  
---|---  
[alignContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-alignContent.html) |  Alignment of the whole area of children on the cross axis if they span over multiple lines in this container.   
[alignItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-alignItems.html) |  Alignment of children on the cross axis of this container.   
[alignSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-alignSelf.html) |  Similar to align-items, but only for this specific element.   
[backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundColor.html) |  Background color to paint in the element's box.   
[backgroundImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundImage.html) |  Background image to paint in the element's box.   
[backgroundPositionX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundPositionX.html) |  Background image x position value.   
[backgroundPositionY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundPositionY.html) |  Background image y position value.   
[backgroundRepeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundRepeat.html) |  Background image repeat value.   
[backgroundSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundSize.html) |  Background image size value. Transitions are fully supported only when using size in pixels or percentages, such as pixel-to-pixel or percentage-to-percentage transitions.   
[borderBottomColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderBottomColor.html) |  Color of the element's bottom border.   
[borderBottomLeftRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderBottomLeftRadius.html) |  The radius of the bottom-left corner when a rounded rectangle is drawn in the element's box.   
[borderBottomRightRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderBottomRightRadius.html) |  The radius of the bottom-right corner when a rounded rectangle is drawn in the element's box.   
[borderBottomWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderBottomWidth.html) |  Space reserved for the bottom edge of the border during the layout phase.   
[borderLeftColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderLeftColor.html) |  Color of the element's left border.   
[borderLeftWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderLeftWidth.html) |  Space reserved for the left edge of the border during the layout phase.   
[borderRightColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderRightColor.html) |  Color of the element's right border.   
[borderRightWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderRightWidth.html) |  Space reserved for the right edge of the border during the layout phase.   
[borderTopColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderTopColor.html) |  Color of the element's top border.   
[borderTopLeftRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderTopLeftRadius.html) |  The radius of the top-left corner when a rounded rectangle is drawn in the element's box.   
[borderTopRightRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderTopRightRadius.html) |  The radius of the top-right corner when a rounded rectangle is drawn in the element's box.   
[borderTopWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-borderTopWidth.html) |  Space reserved for the top edge of the border during the layout phase.   
[bottom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-bottom.html) |  Bottom distance from the element's box during layout.   
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-color.html) |  Color to use when drawing the text of an element.   
[cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-cursor.html) |  Mouse cursor to display when the mouse pointer is over an element.   
[display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-display.html) |  Defines how an element is displayed in the layout.   
[flexBasis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-flexBasis.html) |  Initial main size of a flex item, on the main flex axis. The final layout might be smaller or larger, according to the flex shrinking and growing determined by the other flex properties.   
[flexDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-flexDirection.html) |  Direction of the main axis to layout children in a container.   
[flexGrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-flexGrow.html) |  Specifies how the item will grow relative to the rest of the flexible items inside the same container.   
[flexShrink](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-flexShrink.html) |  Specifies how the item will shrink relative to the rest of the flexible items inside the same container.   
[flexWrap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-flexWrap.html) |  Placement of children over multiple lines if not enough space is available in this container.   
[fontSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-fontSize.html) |  Font size to draw the element's text.   
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-height.html) |  Fixed height of an element for the layout.   
[justifyContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-justifyContent.html) |  Justification of children on the main axis of this container.   
[left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-left.html) |  Left distance from the element's box during layout.   
[letterSpacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-letterSpacing.html) |  Increases or decreases the space between characters.   
[marginBottom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-marginBottom.html) |  Space reserved for the bottom edge of the margin during the layout phase.   
[marginLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-marginLeft.html) |  Space reserved for the left edge of the margin during the layout phase.   
[marginRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-marginRight.html) |  Space reserved for the right edge of the margin during the layout phase.   
[marginTop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-marginTop.html) |  Space reserved for the top edge of the margin during the layout phase.   
[maxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-maxHeight.html) |  Maximum height for an element, when it is flexible or measures its own size.   
[maxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-maxWidth.html) |  Maximum width for an element, when it is flexible or measures its own size.   
[minHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-minHeight.html) |  Minimum height for an element, when it is flexible or measures its own size.   
[minWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-minWidth.html) |  Minimum width for an element, when it is flexible or measures its own size.   
[opacity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-opacity.html) |  Specifies the transparency of an element and of its children.   
[overflow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-overflow.html) |  How a container behaves if its content overflows its own box.   
[paddingBottom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-paddingBottom.html) |  Space reserved for the bottom edge of the padding during the layout phase.   
[paddingLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-paddingLeft.html) |  Space reserved for the left edge of the padding during the layout phase.   
[paddingRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-paddingRight.html) |  Space reserved for the right edge of the padding during the layout phase.   
[paddingTop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-paddingTop.html) |  Space reserved for the top edge of the padding during the layout phase.   
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-position.html) |  Element's positioning in its parent container.   
[right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-right.html) |  Right distance from the element's box during layout.   
[rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-rotate.html) |  A rotation transformation.   
[scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-scale.html) |  A scaling transformation.   
[textOverflow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-textOverflow.html) |  The element's text overflow mode.   
[textShadow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-textShadow.html) |  Drop shadow of the text.   
[top](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-top.html) |  Top distance from the element's box during layout.   
[transformOrigin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transformOrigin.html) |  The transformation origin is the point around which a transformation is applied.   
[transitionDelay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionDelay.html) |  Duration to wait before starting a property's transition effect when its value changes.   
[transitionDuration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionDuration.html) |  Time a transition animation should take to complete.   
[transitionProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionProperty.html) |  Properties to which a transition effect should be applied.   
[transitionTimingFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionTimingFunction.html) |  Determines how intermediate values are calculated for properties modified by a transition effect.   
[translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-translate.html) |  A translate transformation.   
[unityBackgroundImageTintColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityBackgroundImageTintColor.html) |  Tinting color for the element's backgroundImage.   
[unityEditorTextRenderingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityEditorTextRenderingMode.html) |  TextElement editor rendering mode.   
[unityFont](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityFont.html) |  Font to draw the element's text, defined as a Font object.   
[unityFontDefinition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityFontDefinition.html) |  Font to draw the element's text, defined as a FontDefinition structure. It takes precedence over -unity-font.   
[unityFontStyleAndWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityFontStyleAndWeight.html) |  Font style and weight (normal, bold, italic) to draw the element's text.   
[unityOverflowClipBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityOverflowClipBox.html) |  Specifies which box the element content is clipped against.   
[unityParagraphSpacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityParagraphSpacing.html) |  Increases or decreases the space between paragraphs.   
[unitySliceBottom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unitySliceBottom.html) |  Size of the 9-slice's bottom edge when painting an element's background image.   
[unitySliceLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unitySliceLeft.html) |  Size of the 9-slice's left edge when painting an element's background image.   
[unitySliceRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unitySliceRight.html) |  Size of the 9-slice's right edge when painting an element's background image.   
[unitySliceScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unitySliceScale.html) |  Scale applied to an element's slices.   
[unitySliceTop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unitySliceTop.html) |  Size of the 9-slice's top edge when painting an element's background image.   
[unitySliceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unitySliceType.html) |  Specifies the type of sclicing.   
[unityTextAlign](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityTextAlign.html) |  Horizontal and vertical text alignment in the element's box.   
[unityTextGenerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityTextGenerator.html) |  Switches between Unity's standard and advanced text generator   
[unityTextOutlineColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityTextOutlineColor.html) |  Outline color of the text.   
[unityTextOutlineWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityTextOutlineWidth.html) |  Outline width of the text.   
[unityTextOverflowPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-unityTextOverflowPosition.html) |  The element's text overflow position.   
[visibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-visibility.html) |  Specifies whether or not an element is visible.   
[whiteSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-whiteSpace.html) |  Word wrap over multiple lines if not enough space is available to draw the text of an element.   
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-width.html) |  Fixed width of an element for the layout.   
[wordSpacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-wordSpacing.html) |  Increases or decreases the space between words.   
* * *
