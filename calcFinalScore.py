from utils.MatrixPrototypes import *
from evals import *
#import area
#import edgeLengthVariance
#from checkDistributedEdges import *
#import intersections

def calcFinalScore(matrix, solution):
    # still need to implement the "check if nodes are too close" test

    # each score is weighted in order of importance
    # feel free to change weights, this is just a rough estimate of how
    # important different scores are
    if(checkOverlappingPoints.checkOverlappingPoints(matrix, solution) == False):
        return 0.0;
    length = len(solution)
    areaScore, diagonal = area.area(solution)
#    areaScore = 0 * (len(solution) / areaScore)
#    areaScore = 100 * (length / areaScore)
    edgeVarianceScore = 30 * length * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    distEdgeScore = 15 * length * checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectionsScore = 55 * length * intersections.score(matrix, solution)

    return areaScore + edgeVarianceScore + distEdgeScore + intersectionsScore

if __name__=='__main__':
    import sampleGraph
    import randomPermutation
    print(calcFinalScore(sampleGraph.matrix, randomPermutation.points))
