class UserInfo(models.Model):
    #id列，自增，主键
    #创建用户名列，字符串类型，指定长度
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64,db_column='cp')
    createtime=models.DateTimeField(auto_now=True,null=True)
    updatetime=models.DateTimeField(auto_now_add=True,null=True)


'''
字段的参数：
			null               -> db是否可以为空
			default            -> 默认值
			primary_key        -> 主键
			db_column          -> 列名  password=models.CharField(max_length=64,db_column='cp')
			db_index           -> 索引 password=models.CharField(max_length=64,db_index=True)
			unique			   -> 唯一索引
			unique_for_date    -> 对时间做索引
			unique_for_month      对月做索引
			unique_for_year       对年做索引
			
      auto_now           -> 创建时，自动生成时间
			auto_now_add       -> 更新时，自动更新为当前时间
				  # obj = UserGroup.objects.filter(id=1).update(caption='CEO') #不更新auto_now_add
          #如下会更新auto_now_add
	  			# obj = UserGroup.objects.filter(id=1).first()
		  		# obj.caption = "CEO"
			  	# obj.save()
				
	    choices			  -> django admin中显示下拉框，避免连表查询
          user_type_choices=(
              (1,'chaoshiyonghu'),
              (2,'putongyonghu')
          )
          user_type_id=models.IntegerField(choices=user_type_choices,default=1)
			
      blank             -> django admin是否可以为空
			verbose_name      -> django admin显示字段中文
			editable          -> django admin是否可以被编辑
			error_messages    -> 错误信息欠
			help_text         -> django admin提示
			validators		  -> django form ,自定义错误信息（欠）
'''
