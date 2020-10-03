# create-table-query

simply turn this:

```
KHOA
MAKHOA Mã khoa (khóa chính) varchar(4)
TENKHOA Tên khoa varchar(40)
NGTLAP Ngày thành lập khoa smalldatetime
TRGKHOA Trưởng khoa (mã giáo viên) char(4)
```

into this:

```sql
CREATE TABLE dbo.KHOA(
	MAKHOA varchar(4) NOT NULL PRIMARY KEY,
	TENKHOA varchar(40),
	NGTLAP smalldatetime,
	TRGKHOA char(4),
);
```
