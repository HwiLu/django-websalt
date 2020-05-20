from django.db import models

# Create your models here.


## ip
class Ipaddr(models.Model):
    ip = models.GenericIPAddressField(verbose_name="服务器IP", unique=True, help_text="服务器IP地址")
    pod = models.CharField(max_length=10, verbose_name="pod", help_text="网域")
    choice_list = [
        (0, '虚拟机'),
        (1, "物理机")
    ]
    machina_type = models.IntegerField(choices=choice_list, verbose_name="机器类型")

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name_plural = "服务器列表"

# 操作系统
class Os(models.Model):
    os_version = models.CharField(max_length=64)
    os_num = models.CharField(max_length=16)

    def __str__(self):
        return self.os_version

# minion信息
class MinionInfo(models.Model):
    sys_type = models.CharField(max_length=20, unique=True)

    status_chioce = [
        ("0", "stop"),
        ("1", "running")
    ]
    minion_status = models.CharField(max_length=20, choices=status_chioce, verbose_name="minion状态")
    add_time = models.DateTimeField('date added')
    host_ip = models.ForeignKey(Ipaddr, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-add_time', )
        verbose_name_plural = "minion信息"
    def __str__(self):
        return self.sys_type

class JobInfo(models.Model):
    job_id = models.IntegerField(unique=True)

    job_status_choice = [
        ("running", "running"),
        ("done", "done"),
        ("failed", "failed")
    ]
    job_status = models.CharField(max_length=10,choices=job_status_choice, unique=True, verbose_name="作业执行状态")
