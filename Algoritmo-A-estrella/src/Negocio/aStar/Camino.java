package Negocio.aStar;



import java.util.ArrayList;

public class Camino {
	   
        private ArrayList<Nodo> coordenadasCamino = new ArrayList<Nodo>();
        
        public Camino() {
        }
        //devuelve el tama�o del camino
        public int getLength() {
                return coordenadasCamino.size();
        }

        public Nodo getCoordenadasCamino(int index) {
                return coordenadasCamino.get(index);
        }

     
        public int getX(int index) {
                return getCoordenadasCamino(index).getX();
        }

      
        public int getY(int index) {
                return getCoordenadasCamino(index).getY();
        }

       // este a�ade el nodo al final
        public void anadirCordenadas(Nodo n) {
                coordenadasCamino.add(n);
        }

       // este a�ade el nodo al principio
        public void prependWayPoint(Nodo n) {
                coordenadasCamino.add(0, n);
        }

       //comprueba si una posicion pertenece al camino
        public boolean contains(int x, int y) {
                for(Nodo node : coordenadasCamino) {
                        if (node.getX() == x && node.getY() == y)
                                return true;
                }
                return false;
        }

}

