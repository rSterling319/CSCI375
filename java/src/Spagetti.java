package pastas;

public class Spagetti extends Pasta {
	private String _addOn;
	private boolean _cached = false;
	private String _dish = null;
	
	public Spagetti(String addOn){
		_addOn = addOn;
	}
	
	public Spagetti(){
		this("Plain");
	}
	
	private void _updateCache(){
		if (_addOn == "Plain"){
		_dish = "Spagetti with Red Sauce";
		_cached = true;
		}
		else {
		_dish = "Spagetti with " + _addOn;
		_cached = true;
	}
	}
	
	public String getAddOn(){
		return _addOn;
	}
	
	public void setAddOn(String value){
	if(value != _addOn) {
		_addOn = value;
		_cached = false;
	}
	}
	
	public String getDish() {
		if(!_cached) {
			_updateCache();
		}
		return _dish;
	}
}
