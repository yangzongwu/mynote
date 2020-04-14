### Relative Position  
When the position of an element is set to relative, it allows you to specify how CSS should move it relative to its current position in the normal flow of the page. It pairs with the CSS offset properties of left or right, and top or bottom. These say how many pixels, percentages, or ems to move the item away from where it is normally positioned
```html
<style>
  h2 {
    position:relative;
    top:15px;
  }
</style>
<body>
  <h1>On Being Well-Positioned</h1>
  <h2>Move me!</h2>
  <p>I still think the h2 is where it normally sits.</p>
</body>
```
Use CSS offsets to move the h2 15 pixels to the right and 10 pixels up
```html
<style>
  h2 {
    position: relative;
    left:15px;
    bottom:10px;
  }
</style>
```
### Absolute Positioning
One nuance with absolute positioning is that it will be locked relative to its closest positioned ancestor. If you forget to add a position rule to the parent item, (this is typically done using position: relative;), the browser will keep looking up the chain and ultimately default to the body tag.
```html
<style>
  #searchbar {
    position:absolute;
    top:50px;
    right:50px;
  }
  section {
    position: relative;
  }
</style>
```
### Fixed Positioning
One key difference between the fixed and absolute positions is that an element with a fixed position won't move when the user scrolls.
```html
<style>
  #navbar {
    position :fixed;
    top:0px;
    left:0px;
    width: 100%;
    background-color: #767676;
  }
</style>
```

### float
Floating elements are removed from the normal flow of a document and pushed to either the left or right of their containing parent element. It's commonly used with the width property to specify how much horizontal space the floated element requires.
```html
<style>
    #left {
      float:left;
      width: 50%;
    }
    #right {
      float:right;
      width: 40%;
    }
    aside, section {
      padding: 2px;
      background-color: #ccc;
    }
  </style>
```

### Overlapping 
higher values for the z-index property of an element move it higher in the stack than those with lower values.
```html
<style>
{
  .first {
    background-color: red;
    position: absolute;
    z-index:2;

  }
  .second {
    background-color: blue;
    position: absolute;
    left: 40px;
    top: 50px;
    z-index: 1;
  }
</style>

<div class="first"></div>
<div class="second"></div>
```
### Center an Element Horizontally
margin:auto
```html
<style>
  div {
    background-color: blue;
    height: 100px;
    width: 100px;
    margin:auto;
  }
</style>
<div></div>
```
