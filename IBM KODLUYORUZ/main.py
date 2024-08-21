import math

# Tuple'lar içeren 'points' adında bir dizi oluşturuyoruz

points = [(23, 47), (81, 22), (15, 89), (42, 78), (56, 91), (38, 10), (97, 54), (63, 72), (4, 15), (71, 32)]

# Öklid mesafesini hesaplamak üzere 'euclideanDistance' adında bir fonksiyon oluşturuyoruz

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafeleri Hesaplıyoruz

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# En kısa mesafeyi buluyoruz

min_distance = min(distances)

# Sonuçları yazdırıyoruz

print(f"Minimum Mesafe: {min_distance}")