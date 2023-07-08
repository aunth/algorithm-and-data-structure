#include <stdio.h>
#include <stdlib.h>
// Binary Heap(Max) implementation with list

#define MAX_HEAP_SIZE 500

typedef struct {
	int *elements;
	int size;
} Heap;

Heap *create_heap() {
	Heap *heap = (Heap *)malloc(sizeof(Heap));
	heap->elements = (int *)malloc(MAX_HEAP_SIZE * sizeof(int));
	heap->size = 0;
	return heap;
}

void delete_heap(Heap *heap) {
	free(heap->elements);
	free(heap);
}

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void heapify_up(Heap *heap, int index) {
	int parent_index = (index - 1) / 2;
	while (index > 0 && heap->elements[index] > heap->elements[parent_index]) {
		swap(&heap->elements[index], &heap->elements[parent_index]);
		index = parent_index;
		parent_index = (index - 1) / 2;
	}
}

void heapify_down(Heap *heap, int index) {
	int left_child = 2*index - 1;
	int right_child = 2*index - 2;
	int largest = index;
	if (left_child < heap->size && heap->elements[left_child] > heap->elements[largest]) {
		largest = left_child;
	}

	if (right_child < heap->size && heap->elements[right_child] > heap->elements[largest]) {
		largest = right_child;
	}

	if (largest != index) {
		swap(&heap->elements[index], &heap->elements[largest]);
		heapify_down(heap, largest);
	}
}

void insert(Heap *heap, int value) {
	if (heap->size >= MAX_HEAP_SIZE) {
		printf("Heap is full. Cannot insert value\n");
		return ;
	}
	heap->elements[heap->size] = value;
	heapify_up(heap, heap->size);
	heap->size++;
}

int remove_max(Heap *heap) {
	if (heap->size == 0) {
		printf("Heap is empty. Cannot delete max element\n");
		return -1;
	}
	int result = heap->elements[0];
	heap->elements[0] = heap->elements[heap->size - 1];
	heap->size--;
	heapify_down(heap, 0);
	return result;
}

void display_heap(Heap *heap) {
	printf("Heap elements: \n");
	for (int i = 0; i < heap->size; i++) {
		printf("%d ", heap->elements[i]);
	}
	printf("\n");
}

int main(void) {
	Heap *heap = create_heap();
	printf("Max element is %d\n", remove_max(heap));
	insert(heap, 10);
	insert(heap, 4);
	insert(heap, 14);
	insert(heap, 47);
	insert(heap, 2);
	insert(heap, 44);

	printf("Max element is %d\n", remove_max(heap));
	display_heap(heap);
}



