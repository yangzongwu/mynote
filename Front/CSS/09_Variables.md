设置变量：--color  
使用变量：var(--color)  
var(--color,blue),如果变量不存在则选择blue  
```html
<style>
  .one {
    --color--self: red;
  }
  .two {
    background: var(--color--self:,blue);
  }
  #three {
    background: var(--color1--self:,yellow);
  }
</style>
<div class="one">
  <h1 class="two">Hello</h1>
  <h1 id="three">Welcome</h1>
</div>
```
