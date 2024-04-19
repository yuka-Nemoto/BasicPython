a = "How"
b = "I"
c = "want"
d = "a"
e = "drink"
f = "alcoholic"
g = "of"
h = "course"
i = "after"
j = "the"
k = "heavy"
l = "chapters"
m = "involving"
n = "quantum"
o = "mechanics"
p = "All"
q = "of"
r = "thy"
s = "geometry"
t = "Herr"
u = "Planck"
v = "is"
w = "fairly"
x = "hard"

L_int = [len(a), len(b), len(c), len(d), len(e), len(f), len(g), len(h),len(i),len(j),len(k),len(l),len(m),len(n),len(o),len(p),len(q),len(r),len(s),len(t),len(u),len(v),len(w),len(x)]

L = [str(A) for A in L_int]
L = "".join(L)
print(L)