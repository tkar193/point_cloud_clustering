from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import numpy as np
import random

#Creates a set of n points on the first iteration at random
def create_new_dataset(n):
    data_set = []
    for i in range(n):
        data = random.sample(list(np.linspace(0,9.9,num=100)), k=3)
        data_set.append(data)
    #print(data_set)
    return data_set

#Creates new centroids for the clusters, at random for the first iteration
def define_new_centroids_first(data_set, k, n):
    centroids = []
    for i in range(k):
        random_index = random.randrange(n)
        if data_set[random_index] in centroids:
            random_index = random.randrange(n) #Think for a better fix later
        centroids.append(data_set[random_index])
    #print(centroids)
    return centroids

#For every iteration after the first, the centroids are the mean of all the points in that cluster
def define_new_centroids(clusters, k):
    centroids = []
    for i in range(k):
        X = []
        Y = []
        Z = []
        points = clusters[i]
        for point in points:
            X.append(point[0])
            Y.append(point[1])
            Z.append(point[2])
        centroid = [sum(X)/len(X), sum(Y)/len(Y), sum(Z)/len(Z)]
        centroids.append(centroid)

    return centroids

#Helper fucntion to add the data point to the appropriate cluster determined
def add_to_cluster(clusters, data_point, clusters_index):
    clusters[clusters_index].append(data_point)

#Computes the minimum distance for each point in the dataset from the cluster in question
def compute_min_distance(data_point, centroids, k, clusters):
    min_index = None
    min_distance = None
    for i in range(k):
        if centroids[i] is data_point:
            min_index = i
            return
        if min_index is None:
            min_index = i
            min_distance = distance.euclidean(centroids[i], data_point)
            i = i + 1
            continue
        dist = distance.euclidean(centroids[i], data_point)
        if dist < min_distance:
            min_distance = dist
            min_index = i
        i = i + 1
    add_to_cluster(clusters, data_point, min_index)

#Suppose a data_set is a set of multiple points in a 2-D coordinate plane
#k is the number of clusters, also the number of randomly picked initial centroids
#n is the number of data points
def kmeans(data_set, k, n, clusters, count, iterations):
    #Following loop defines the different centroids
    if count is 0:
        centroids = define_new_centroids_first(data_set, k, n)
    elif count < iterations:
        centroids = define_new_centroids(clusters, k)
    elif count == iterations:
        return clusters

    #Define the clusters lists
    for i in range(k):
        clusters.append([centroids[i]])

    #This will calculate which cluster each data point will belong to
    #We do this by calculating the minimum distance from the point to each centroid
    for i in range(n):
        compute_min_distance(data_set[i], centroids, k, clusters)
    return kmeans(data_set, k, n, clusters, count + 1, iterations)

#generate a scatter plot for each cluster individually
def scatter_cluster(points, ax):
    X = []
    Y = []
    Z = []
    for point in points:
        X.append(point[0])
        Y.append(point[1])
        Z.append(point[2])

    #Generate a random color to assign to cluster in question
    r = lambda: random.randint(0,255)
    ax.scatter(X,Y,Z, c = '#%02X%02X%02X' % (r(),r(),r()))

#Show the final scatterplot with the different points colored according to cluster
def show_plot(clusters, k):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(k):
        points = clusters[i]
        scatter_cluster(points, ax)
    plt.show()

def main():
    n = int(input('Enter the desired number of data points: '))
    data_set = create_new_dataset(n)
    k = int(input('Enter the desired number of clusters: '))
    iter = int(input('Enter the desired amount of iterations: '))

    clusters = []
    clusters = kmeans(data_set, k, n, clusters, 0, iter)
    show_plot(clusters, k)

main()
