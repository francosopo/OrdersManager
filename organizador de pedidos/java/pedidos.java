class Lista{
    private int dato; //cambiar tipo
    private Lista cola;
    Lista(int datoo,Lista colaa){ //cambiar tipo
        dato=datoo;
        cola=colaa;
    }
    Lista(){
        dato=0; //cambiar inicialización
        cola=null;
    }
    public int getDato(){ //cambiar tipo 
        return dato;
    }
    public Lista getCola(){
        return cola;
    }
    public void setCola(Lista colaa){
        cola=colaa;
    }
    public static void agregar(int x,Lista l){ //cambiar tipo
        Lista actual = l;
        while(actual.cola!=null){
            actual=actual.cola;
        }
        actual.cola = new Lista(x,null);
    }
    public static void eliminar(int elemento, Lista lista){ //cambiar tipo
        Lista ant=lista;
        Lista act=lista;
        while(act.getDato()!= elemento){
            ant=act;
            act=act.getCola();
        }
        ant.setCola(act.getCola());
        act=act.getCola();
    }
}

class Pila{
    Lista pila;
    Pila(){
        pila=null;
    }
    public void push(int x){ //cambiar tipo 
        pila=new Lista(x,pila);
    }
    public int top(){ //cambiar tipo
        return pila.getDato();
    }
    public int pop(){ //cambiar tipo
        int dato=pila.getDato();
        pila=pila.getCola();
        return dato;
    }
    public boolean estaVacia(){
        return pila==null;
    }
}
class Cliente{
    private String nombre;
    private int cantidad;
    private int precio;
    private String fechaDeEntrega;
    private String modoDePago;
    Cliente(String nombre, int cantidad, int precio,String fechaDeEntrega,String modoDePago){
        this.nombre=nombre;
        this.cantidad=cantidad;
        this.precio=precio;
        this.fechaDeEntrega=fechaDeEntrega;
        this.modoDePago=modoDePago;
    }
    public String getNombre(){
        return this.nombre;
    }
    public int getCantidad(){
        return this.cantidad;
    }
    public int getPrecio(){
        return this.precio;
    }
    public String getFechaDeEntrega(){
        return this.fechaDeEntrega;
    }
    public String getModoDePago(){
        return this.modoDePago;
    }

}
class Arbol{
    private Cliente dato;
    private Arbol izq;
    private Arbol der;
    Arbol(Cliente datoo,Arbol izqq, Arbol derr){
        dato=datoo;
        izq=izqq;
        der=derr;
    }
    public Cliente getDato(){
        return this.dato;
    }
    public Arbol getIzq(){
        return this.izq;
    }
    public Arbol getDer(){
        return this.der;
    }
    public static  boolean menorQue(String a,String b){
        return a.compareTo(b)<0;
    }
    public static boolean mayorQue(String a,String b){
        return a.compareTo(b)>0;
    }
    public static boolean esIgual(String a,String b){
        return a.compareTo(b)==0;
    }
    void agregar(Cliente c){
        if(menorQue(c.getNombre(),this.dato.getNombre())){
            if(this.izq==null){
                this.izq=new Arbol(c,null,null);
            }
            else{
                this.izq.agregar(c);
            }
        }
        else if(mayorQue(c.getNombre(),this.dato.getNombre())){
            if(this.der==null){
                this.der= new Arbol(c,null,null);
            }
            else{
                this.der.agregar(c);
            }
        }
        else{
            System.out.println("Ya existe ese cliente");
        }
    }
    public Cliente getMax(){
        if(this.der==null){
            return this.dato;
        }
        else{
            return this.der.getMax();
        }
    }
    public Cliente getMin(){
        if(this.izq==null){
            return this.dato;
        }
        else{
            return this.izq.getMin();
        }
    }
}
class pedidos{
    public static  boolean menorQue(String a,String b){
        return a.compareTo(b)<0;
    }
    public static boolean mayorQue(String a,String b){
        return a.compareTo(b)>0;
    }
    public static boolean esIgual(String a,String b){
        return a.compareTo(b)==0;
    }
    public static void eliminar(Arbol a,String nombre){
        if(a.getDato().getNombre().equals(nombre)){ 
            if(a.getIzq()==null && a.getDer()==null){
                a=null;
            }
            else if(a.getIzq()==null){
                a=a.getDer();
            }
            else if(a.getDer()== null){
                a=a.getIzq();
            }
            else{
                Cliente c= a.getIzq().getMax();
                eliminar(a.getIzq(),c.getNombre());
                a= new Arbol(c,a.getIzq(),a.getDer());
            }
        }
        else{
            if(menorQue(nombre,a.getDato().getNombre())){
                eliminar(a.getIzq(),nombre);
            }
            else{
                eliminar(a.getDer(),nombre);
            }
        }
       
    }
    
    public static void main(String[] args){
        Cliente uno = new Cliente("Francisco",5,5000,"25-06-2019","efectivo");
        Cliente dos = new Cliente("Nadia",7,7000,"26-06-2019","transferencia");
        Cliente tres = new Cliente("Ariel",2,2000,"25-06-2019","efectivo");
        Arbol a=new Arbol(uno,null,null);
        a.agregar(dos);
        a.agregar(tres);
        eliminar(a,"Nadia");
        System.out.println(a.getDer().getDato().getNombre());
    }
}